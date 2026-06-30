from app.config import IMAGE_DIR
from app.vision.caption import generate_caption


image_path = IMAGE_DIR / "figure-3-1.jpg"

caption = generate_caption(image_path)

print("=" * 60)
print(caption)
print("=" * 60)