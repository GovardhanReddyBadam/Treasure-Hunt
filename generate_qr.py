import segno
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://unsiccative-ronni-paniculately.ngrok-free.dev"
LOGO_PATH = "math_logo.png"

BACKGROUND_COLORS = [
    "#0f5f78",
    "#1e3a8a",
    "#166534",
    "#7c2d12",
    "#6b21a8",
]

def rounded_rect(size, radius, color):
    img = Image.new("RGBA", size)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, *size), radius, fill=255)
    img.paste(color, mask=mask)
    return img

def add_footer(img, bg):
    w, h = img.size
    footer_h = int(h * 0.28)

    out = Image.new("RGB", (w, h + footer_h), bg)
    out.paste(img, (0, 0))

    draw = ImageDraw.Draw(out)
    try:
        font = ImageFont.truetype("arial.ttf", 46)
    except:
        font = ImageFont.load_default()

    text = "Scan me!"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]

    draw.text(
        ((w - tw)//2, h + (footer_h - th)//2),
        text,
        fill="white",
        font=font
    )
    return out

for i in range(1, 91):
    bg = BACKGROUND_COLORS[(i - 1) % 5]

    qr = segno.make(f"{BASE_URL}/hunt/{i}", error="h")

    qr.save(
        "temp_qr.png",
        scale=10,
        dark="black",
        light="white"
    )

    qr_img = Image.open("temp_qr.png").convert("RGBA")

    # white rounded card
    pad = 35
    card = rounded_rect(
        (qr_img.width + pad*2, qr_img.height + pad*2),
        radius=40,
        color="white"
    )
    card.paste(qr_img, (pad, pad), qr_img)

    # center logo
    logo = Image.open(LOGO_PATH).convert("RGBA")
    size = card.width // 4
    logo = logo.resize((size, size))

    pos = ((card.width - size)//2, (card.height - size)//2)
    card.paste(logo, pos, logo)

    # colored background frame
    frame_pad = 40
    frame = Image.new(
        "RGB",
        (card.width + frame_pad*2, card.height + frame_pad*2),
        bg
    )
    frame.paste(card, (frame_pad, frame_pad))

    final = add_footer(frame, bg)
    final.save(f"qr_{i}.png")

print("✅ 90 QRs generated (style-matched)")
