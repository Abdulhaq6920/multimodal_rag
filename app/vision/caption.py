import base64
from pathlib import Path

from groq import Groq

from app.config import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)


def _image_to_base64(image_path: str) -> str:
    """
    Convert an image into Base64.
    """

    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode("utf-8")


def generate_caption(image_path: str) -> str:
    """
    Generate a searchable caption for an image.
    """

    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(
            f"{image_path} not found."
        )

    image_base64 = _image_to_base64(image_path)

    response = client.chat.completions.create(
        model=settings.GROQ_VISION_MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "You generate captions for a Multimodal "
                    "Retrieval-Augmented Generation system.\n\n"
                    "Describe only what is visible.\n"
                    "Focus on diagrams, charts, flowcharts, "
                    "tables, screenshots and important labels.\n"
                    "Do not guess.\n"
                    "Return only the description."
                ),
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate a detailed searchable caption."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    },
                ],
            },
        ],
    )

    return response.choices[0].message.content.strip()