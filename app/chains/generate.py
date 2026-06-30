from typing import Iterator

from app.llm.groq import (
    llm,
    streaming_llm,
)
from app.llm.prompt import chat_prompt


def _build_prompt(
    question: str,
    context: str,
    history: list,
):
    """
    Build the chat prompt.
    """

    return chat_prompt.invoke(
        {
            "history": history,
            "context": context,
            "question": question,
        }
    )


def generate_answer(
    question: str,
    context: str,
    history: list,
) -> str:
    """
    Generate the complete answer.
    """

    prompt = _build_prompt(
        question=question,
        context=context,
        history=history,
    )

    response = llm.invoke(prompt)

    return response.content


def stream_answer(
    question: str,
    context: str,
    history: list,
) -> Iterator[str]:
    """
    Stream the answer token by token.
    """

    prompt = _build_prompt(
        question=question,
        context=context,
        history=history,
    )

    for chunk in streaming_llm.stream(prompt):

        if chunk.content:
            yield chunk.content