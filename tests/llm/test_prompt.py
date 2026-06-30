from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)

from app.llm.prompt import chat_prompt


prompt = chat_prompt.invoke(
    {
        "history": [
            HumanMessage(
                content="What is a Transformer?"
            ),
            AIMessage(
                content="A Transformer is a neural network architecture."
            ),
        ],
        "context": """
Transformers replace recurrence with self-attention mechanisms,
allowing parallel computation over sequences.
""",
        "question": "Explain self-attention.",
    }
)


print("=" * 60)
print("Formatted Prompt")
print("=" * 60)

for message in prompt.messages:
    print(f"\n{type(message).__name__}")
    print("-" * 60)
    print(message.content)

print("\n" + "=" * 60)