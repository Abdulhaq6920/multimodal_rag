from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.api.models import (
    ChatRequest,
    ChatResponse,
)
from app.chains.generate import (
    generate_answer,
    stream_answer,
)
from app.chains.retrieve import retrieve_documents
from app.memory.history import (
    add_ai_message,
    add_human_message,
    get_chat_history,
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "/",
)
async def chat(request: ChatRequest):
    """
    Normal (non-streaming) chat endpoint.
    """

    retrieval = retrieve_documents(
        request.question
    )

    answer = generate_answer(
        question=request.question,
        context=retrieval["context"],
        history=get_chat_history(),
    )

    add_human_message(request.question)
    add_ai_message(answer)

    return {
        "answer": answer,
        "sources": retrieval["sources"],
    }


@router.post("/stream")
async def stream_chat(
    request: ChatRequest,
):
    """
    Streaming chat endpoint.
    """

    retrieval = retrieve_documents(
        request.question
    )

    history = get_chat_history()

    def event_generator():

        complete_answer = ""

        for token in stream_answer(
            question=request.question,
            context=retrieval["context"],
            history=history,
        ):

            complete_answer += token

            yield token

        add_human_message(request.question)
        add_ai_message(complete_answer)

    return StreamingResponse(
        event_generator(),
        media_type="text/plain",
    )


@router.get("/history")
async def chat_history():
    """
    Debug endpoint.
    """

    history = get_chat_history()

    return [
        {
            "type": message.__class__.__name__,
            "content": message.content,
        }
        for message in history
    ]