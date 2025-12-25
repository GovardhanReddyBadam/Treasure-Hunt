# 🔐 QR-Based Secure Treasure Hunt Web Application

An interactive, QR-code–driven treasure hunt platform built using **Python** and **Flask**, designed for events, classrooms, and competitions.  
Each QR code unlocks a **password-protected clue** (text and/or image), guiding users step-by-step toward the final destination.

---

## 📌 Project Overview

This project implements a **secure, multi-QR treasure hunt system** where:
- Each QR code maps to a unique route
- Access is protected using passwords and sessions
- The password for the next QR is the answer for the question diplayed in the present QR
- Clues can include riddles, questions, and images
- The application can be accessed **across different devices and networks**

It is designed as a **real-world, event-ready application**, not just a demo.

---

## 🎯 Use Cases

- 🏫 School & college competitions  
- 🎉 Technical fests and events  
- 🧠 Puzzle & logic hunts  
- 📚 Interactive learning activities  
- 🏢 Team-building games  

---

## ✨ Features

- 🔐 Password-protected QR routes  
- 🔢 Unique password for each QR code  
- 🧠 Text-based and image-based clues  
- ⏱️ Optional time-delayed image reveal  
- 🧾 Session-based authentication (prevents direct URL access)  
- 🎨 Themed QR codes with multiple background colors  
- 📱 Works on mobile, tablet, and desktop devices  
- 🌐 Public access using **ngrok**  
- ⚙️ Automated generation of 90+ QR codes  

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **QR Generation:** segno, Pillow  
- **Tunneling:** ngrok  
- **Version Control:** Git & GitHub  

---

## 🏗️ Project Structure
Password Qrs/
│
├── app.py # Main Flask application   
├── generate_qr.py # Script to generate QR codes   
├── templates/   
│ ├── login.html # Password input page     
├── static/   
│ └── clues/ # Clue images (local)   
│ └── secure.html # Clue display page
├── requirements.txt   
├── .gitignore   
└── README.md



---

## ⚙️ How the Application Works

1. User scans a QR code  
2. QR opens a route like `/hunt/<id>`  
3. Flask displays a password page  
4. On correct password:
   - A session is created
   - User is redirected to `/clue/<id>`
5. Question is shown immediately  
6. Clue image (if any) is shown after a delay  
7. User proceeds to the next location  

---

## 🔐 Security Design

- Password validation for every QR  
- Flask sessions prevent unauthorized access  
- Direct URL access is blocked without authentication  
- High QR error correction allows safe logo embedding  

---

## 🧩 QR Code Generation

- QR codes are generated in bulk (1–70)
- Each QR points to a unique URL
- 5 rotating background color themes
- Central math-themed logo embedded
- High scannability ensured
NOTE:ignore the QRs in the repository they are for only referential purpose generate your own QRs using ganerate_qr.py

---

## 🌐 Public Access Using ngrok

### Why ngrok?
Local servers (`127.0.0.1`) are not accessible from other devices.  
**ngrok creates a secure public tunnel** to your local Flask app.

### Steps to use ngrok:
1. Install ngrok from https://ngrok.com  
2. ```bash: ngrok config add-authtoken YOUR_TOKEN
3.Run Flask:python app.py   
4.In another terminal:ngrok http 5000   
5.Use the generated public URL in QR generation




📚 Learning Outcomes

Through this project, I gained hands-on experience in:

Flask routing and session management

Secure web application design

QR code generation and customization

Image handling with Pillow

Debugging real-world deployment issues

Git & GitHub workflows

Networking concepts (localhost vs public URLs)

🏁 Conclusion

This project demonstrates an end-to-end full-stack workflow, combining backend logic, frontend rendering, security, automation, and deployment concepts.
It is suitable for academic evaluation, LinkedIn showcasing, and real event usage.

⭐ If you find this project useful, feel free to star the repository!
