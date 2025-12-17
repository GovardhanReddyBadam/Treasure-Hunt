import qrcode

BASE = "http://10.246.221.69:5000"

for i in range(1, 5):
    qrcode.make(f"{BASE}/hunt/{i}").save(f"qr_{i}.png")

print("QRs created")