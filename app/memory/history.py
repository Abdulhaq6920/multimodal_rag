from collections import deque

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)


MAX_HISTORY = 10

_history = deque(maxlen=MAX_HISTORY)


def add_human_message(message: str):
    """
    Store a HumanMessage.
    """
    _history.append(
        HumanMessage(content=message)
    )


def add_ai_message(message: str):
    """
    Store an AIMessage.
    """
    _history.append(
        AIMessage(content=message)
    )


def get_chat_history():
    """
    Return all stored messages.
    """
    return list(_history)


def clear_chat_history():
    """
    Clear the conversation history.
    """
    _history.clear()