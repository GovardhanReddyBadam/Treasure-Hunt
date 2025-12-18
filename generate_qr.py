import qrcode

# ✅ DEFINE BASE_URL FIRST
BASE_URL = "https://unsiccative-ronni-paniculately.ngrok-free.dev"
# OR (for local testing)
# BASE_URL = "http://127.0.0.1:5000"

for i in range(1, 71):
    img = qrcode.make(f"{BASE_URL}/hunt/{i}")
    img.save(f"qr_{i}.png")

print("QR codes generated successfully")
