from flask import Flask, render_template, request, redirect, session, url_for

# ✅ CREATE FLASK APP (MISSING BEFORE)
app = Flask(__name__)

# ✅ REQUIRED FOR SESSIONS
app.secret_key = "treasure_secret_key_123"

# 🗺️ Clues for each QR
CLUES = {
    "1": {
        "text": "Find the next number: 2, 6, 12, 20,__",
        "image": "clues/clue1.jpg"
    },
    "2": {
        "text": "What is the smallest prime number?",
        "image": "clues/clue2.jpg"
    },
    "3": {
        "text": "Find the odd one out: 2, 3, 5, 9, 11",
        "image": "clues/clue3.jpg"
    },
    "4": {
        "text": "Find the next number: 1, 1, 2, 3, 5, ___",
        "image": "clues/clue4.jpg"
    },
    "5": {
        "text": "If TODAY = 555, find MATH",
        "image": "clues/clue5.jpg"
    },
    "6": {
        "text": "Sum of first 10 natural numbers",
        "image": "clues/clue6.jpg"
    },
    "7": {
        "text": " Find the missing number: 4, 9, 16, ___, 36",
        "image": "clues/clue7.jpg"
    },
    "8": {
        "text": " How many factors does 12 have?",
        "image": "clues/clue8.jpg"
    },
    "9": {
        "text": "What is the only even prime number?",
        "image": "clues/clue9.jpg"
    },
    "10": {
        "text": "Find the LCM of 4 and 6",
        "image": "clues/clue10.jpg"
    },
    "11": {
        "text": "Find the HCF of 18 and 24",
        "image": "clues/clue11.jpg"
    },
    "12": {
        "text": "What is 25 percent 0f 200?",
        "image": "clues/clue12.jpg"
    },
    "13": {
        "text": "How many digits are there in the number 1000?",
        "image": "clues/clue13.jpg"
    },
    "14": {
        "text": "What is the value of 7³?",
        "image": "clues/clue14.jpg"
    },
    "15": {
        "text": "How many zeros are there in one thousand?",
        "image": "clues/clue15.jpg"
    },
    "16": {
        "text": "Solve: 2x = 10",
        "image": "clues/clue16.jpg"
    },
    "17": {
        "text": "Solve: x + 7 = 15",
        "image": "clues/clue17.jpg"
    },
    "18": {
        "text": "Solve: 3x - 6 = 9",
        "image": "clues/clue18.jpg"
    },
    "19": {
        "text": "If x = 4, find x² + 2x",
        "image": "clues/clue19.jpg"
    },
    "20": {
        "text": " Solve: 5x = 25",
        "image": "clues/clue20.jpg"
    },
    "21": {
        "text": "Find x: x/4 = 5",
        "image": "clues/clue21.jpg"
    },
    "22": {
        "text": "If a = 3 and b = 2, find a² - b²",
        "image": "clues/clue22.jpg"
    },
    "23": {
        "text": "Solve: 2(x + 3) = 14",
        "image": "clues/clue23.jpg"
    },
    "24": {
        "text": "If x + y = 10 and y = 4, find x",
        "image": "clues/clue24.jpg"
    },
    "25": {
        "text": "Solve: x² = 16 (positive root)",
        "image": "clues/clue25.jpg"
    },
    "26": {
        "text": " Solve: 4x - 8 = 0",
        "image": "clues/clue26.jpg"
    },
    "27": {
        "text": "If x = 3, find 2x²",
        "image": "clues/clue27.jpg"
    },
    "28": {
        "text": "Solve: 6x = 36",
        "image": "clues/clue28.jpg"
    },
    "29": {
        "text": "Find x: x - 9 = 11",
        "image": "clues/clue29.jpg"
    },
    "30": {
        "text": "Solve: x² - 9 = 0 (positive root)",
        "image": "clues/clue30.jpg"
    },
    "31": {
        "text": "Number of sides in a hexagon",
        "image": "clues/clue31.jpg"
    },
    "32": {
        "text": "Sum of angles of a triangle (degrees)",
        "image": "clues/clue32.jpg"
    },
    "33": {
        "text": "Area of square of side 6",
        "image": "clues/clue33.jpg"
    },
    "34": {
        "text": "Perimeter of rectangle (length 8, breadth 5)",
        "image": "clues/clue34.jpg"
    },
    "35": {
        "text": "Degrees in a right angle",
        "image": "clues/clue35.jpg"
    },
    "36": {
        "text": "Number of faces of a cube",
        "image": "clues/clue36.jpg"
    },
    "37": {
        "text": "Area of rectangle (10 * 4)",
        "image": "clues/clue37.jpg"
    },
    "38": {
        "text": "Radius if diameter is 14",
        "image": "clues/clue38.jpg"
    },
    "39": {
        "text": "Number of diagonals in a square",
        "image": "clues/clue39.jpg"
    },
    "40": {
        "text": "Volume of cube of side 3",
        "image": "clues/clue40.jpg"
    },
    "41": {
        "text": "Number of vertices of a square pyramid",
        "image": "clues/clue41.jpg"
    },
    "42": {
        "text": "Area of triangle (base 10, height 6)",
        "image": "clues/clue42.jpg"
    },
    "43": {
        "text": "Number of edges in a cube",
        "image": "clues/clue43.jpg"
    },
    "44": {
        "text": "Number of angles in a quadrilateral",
        "image": "clues/clue44.jpg"
    },
    "45": {
        "text": "Number of sides in a decagon",
        "image": "clues/clue45.jpg"
    },
    "46": {
        "text": "ind the next number: 5, 10, 20, 40, ___",
        "image": "clues/clue46.jpg"
    },
    "47": {
        "text": "Find the next number: 1, 4, 9, 16, ___",
        "image": "clues/clue47.jpg"
    },
    "48": {
        "text": "Find the next number: 2, 3, 5, 7, ___",
        "image": "clues/clue48.jpg"
    },
    "49": {
        "text": "Find the next number: 3, 6, 9, ___, 15",
        "image": "clues/clue49.jpg"
    },
    "50": {
        "text": "Find the next number: 100, 90, 80, ___",
        "image": "clues/clue50.jpg"
    },
    "51": {
        "text": "Find the next number: 1, 8, 27, ___",
        "image": "clues/clue51.jpg"
    },
    "52": {
        "text": "Find the next number: 2, 4, 8, ___, 32",
        "image": "clues/clue52.jpg"
    },
    "53": {
        "text": "Find the next number: 10, 20, 40, ___",
        "image": "clues/clue53.jpg"
    },
    "54": {
        "text": "Find the next number: 7, 14, 21, ___",
        "image": "clues/clue54.jpg"
    },
    "55": {
        "text": "Find the next number: 1, 2, 4, 7, 11, ___",
        "image": "clues/clue55.jpg"
    },
    "56": {
        "text": "Find the missing number: 2, 6, 18, ___",
        "image": "clues/clue56.jpg"
    },
    "57": {
        "text": "Find the missing number: 81, 27, 9, ___",
        "image": "clues/clue57.jpg"
    },
    "58": {
        "text": "Find the missing number: 1, 3, 6, 10, ___",
        "image": "clues/clue58.jpg"
    },
    "59": {
        "text": "Find the missing number: 4, 16, 36, ___",
        "image": "clues/clue59.jpg"
    },
    "60": {
        "text": "Find the missing number: 11, 22, 33, ___",
        "image": "clues/clue60.jpg"
    },
    "61": {
        "text": "12 * 5",
        "image": "clues/clue61.jpg"
    },
    "62": {
        "text": "144 ÷ 12",
        "image": "clues/clue62.jpg"
    },
    "63": {
        "text": "7²",
        "image": "clues/clue63.jpg"
    },
    "64": {
        "text": "√81",
        "image": "clues/clue64.jpg"
    },
    "65": {
        "text": " 9 * 11",
        "image": "clues/clue65.jpg"
    },
    "66": {
        "text": "One step away to the Treasure '-_-'",
        "image": "clues/clue66.jpg"
    },
    "67": {
        "text": "One step away to the Treasure '-_-'",
        "image": "clues/clue67.jpg"
    },
    "68": {
        "text": "One step away to the Treasure '-_-'",
        "image": "clues/clue68.jpg"
    },
    "69": {
        "text": "One step away to the Treasure '-_-'",
        "image": "clues/clue69.jpg"
    },
    "70": {
        "text": "One step away to the Treasure '-_-'",
        "image": "clues/clue70.jpg"
    }
}

# 🔐 Different password for each QR
PASSWORDS = {
    "1":"maths",
    "2":"maths",
    "3":"maths",
    "4":"maths",
    "5":"maths",
    "6":"30",
    "7":"2",
    "8":"9",
    "9":"8",
    "10":"42",
    "11":"55",
    "12":"25",
    "13":"6",
    "14":"2",
    "15":"12",
    "16":"6",
    "17":"50",
    "18":"4",
    "19":"343",
    "20":"3",
    "21":"5",
    "22":"8",
    "23":"5",
    "24":"24",
    "25":"5",
    "26":"20",
    "27":"5",
    "28":"4",
    "29":"6",
    "30":"4",
    "31":"2",
    "32":"18",
    "33":"6",
    "34":"20",
    "35":"3",
    "36":"6",
    "37":"180",
    "38":"36",
    "39":"26",
    "40":"90",
    "41":"6",
    "42":"40",
    "43":"7",
    "44":"2",
    "45":"27",
    "46":"5",
    "47":"30",
    "48":"12",
    "49":"4",
    "50":"10",
    "51":"80",
    "52":"25",
    "53":"11",
    "54":"12",
    "55":"70",
    "56":"64",
    "57":"16",
    "58":"80",
    "59":"28",
    "60":"16",
    "61":"54",
    "62":"3",
    "63":"15",
    "64":"64",
    "65":"44",
    "66":"60",
    "67":"12",
    "68":"49",
    "69":"9",
    "70":"99",
    "71":"55",
    "72":"50",
    "73":"6",
    "74":"343",
    "75":"12",
    "76":"5",
    "77":"18",
    "78":"7",
    "79":"20",
    "80":"4",
    "81":"6",
    "82":"30",
    "83":"80",
    "84":"12",
    "85":"90",
    "86":"54",
    "87":"16",
    "88":"15",
    "89":"28",
    "90":"70",        
    
}

@app.route("/hunt/<qr_id>", methods=["GET", "POST"])
def hunt(qr_id):
    if qr_id not in CLUES:
        return "Invalid QR code"

    if request.method == "POST":
        if request.form.get("password") == PASSWORDS[qr_id]:
            session[f"qr_{qr_id}"] = True
            return redirect(url_for("clue", qr_id=qr_id))
        return "❌ Ee answer chusi calculator kuda silent ayyindhi!"

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
    app.run(
        #Enter the host According to your network
        host="*",
        #Enter the port that given by the ngrok
        port=*,
        debug=False,
        use_reloader=False
    )
