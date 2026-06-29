from PIL import Image, ImageDraw, ImageFont
import os

# ========== SETTINGS ==========
WIDTH, HEIGHT = 1280, 760 # Fiverr کا سائز
BG_COLOR = "#1DB954" # Fiverr Green
TEXT_COLOR = "#FFFFFF" # White Text
SHADOW_COLOR = "#000" # Black Shadow
BORDER_COLOR = "#FFFFFF" # White Border
FONT_SIZE = 220 # بہت بڑا Font
BORDER_WIDTH = 20 # موٹا Border
OUTPUT_FOLDER = "output"

# ========== TEXT = 3 WORDS MAX ==========
GIG_TITLES = [
    "PYTHON DJANGO",
    "SAAS DEVELOPER",
    "BILLING EXPERT",
    "FIVERR GIG"
]

def create_thumbnail(text):
    # 1. Blank Green Image
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 2. ExtraBold Font - نہیں ملا تو Default لے لو
    try:
        font = ImageFont.truetype("Poppins-ExtraBold.ttf", FONT_SIZE)
    except:
        font = ImageFont.load_default()

    # 3. Text Size نکالو Center کرنے کے لیے
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (WIDTH - text_width) / 2
    y = (HEIGHT - text_height) / 2

    # 4. BLACK SHADOW پہلے لگاؤ = Text Pop کرے گا
    for offset in range(8, 0, -1): # 8 سے 1 تک Shadow
        draw.text((x + offset, y + offset), text, font=font, fill=SHADOW_COLOR)

    # 5. WHITE TEXT اوپر لکھو
    draw.text((x, y), text, font=font, fill=TEXT_COLOR)

    # 6. WHITE BORDER لگاؤ = Fiverr پر Stand Out
    draw.rectangle([20, 20, WIDTH-20, HEIGHT-20], outline=BORDER_COLOR, width=BORDER_WIDTH)

    # 7. Save کرو
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    img.save(f"{OUTPUT_FOLDER}/{text.replace(' ', '_')}.png")
    print(f"Saved: {text}")

if __name__ == "__main__":
    for title in GIG_TITLES:
        create_thumbnail(title)
    print(f"All Pro Thumbnails Generated in /{OUTPUT_FOLDER} folder")