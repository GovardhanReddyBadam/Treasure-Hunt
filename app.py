from flask import Flask, render_template, request, redirect, session, url_for

# ✅ CREATE FLASK APP (MISSING BEFORE)
app = Flask(__name__)

# ✅ REQUIRED FOR SESSIONS
app.secret_key = "treasure_secret_key_123"

# 🗺️ Clues for each QR
CLUES = {
    "1": {
        "text": "Find the next number: 2, 6, 12, 20,----",
        "image": "clues/clue1.jpg"
    },
    "2": {
        "text": "Riddle:\nI am the home of zero noise and infinite knowledge.\nNumbers sleep on pages, not on screens.\nWhere am I?",
        "image": "clues/clue2.jpg"
    },
    "3": {
        "text": "Check the notice board near the main gate 🚪",
        "image": "clues/clue3.jpg"
    },
    "4": {
        "text": "🎉 Final treasure is behind the red door 🔑",
        "image": "clues/clue4.jpg"
    }
}

# 🔐 Different password for each QR
PASSWORDS = {
    "1": "oak123",
    "2": "30",
    "3": "gate789",
    "4": "treasure999"
}

@app.route("/hunt/<qr_id>", methods=["GET", "POST"])
def hunt(qr_id):
    if qr_id not in CLUES:
        return "Invalid QR code"

    if request.method == "POST":
        if request.form.get("password") == PASSWORDS[qr_id]:
            session[f"qr_{qr_id}"] = True
            return redirect(url_for("clue", qr_id=qr_id))
        return "❌ Wrong password"

    return render_template("login.html")

@app.route("/clue/<qr_id>")
def clue(qr_id):
    if not session.get(f"qr_{qr_id}"):
        return redirect(url_for("hunt", qr_id=qr_id))

    return render_template(
        "secure.html",
        clue_text=CLUES[qr_id]["text"],
        clue_image=CLUES[qr_id]["image"]
    )


# ✅ REQUIRED TO START SERVER
if __name__ == "__main__":
    app.run()
