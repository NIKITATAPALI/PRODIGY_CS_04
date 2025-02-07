# 🔑 Advanced Keylogger Project

## 📌 Overview
This project is an **Advanced Keylogger** written in Python. It logs keystrokes and stores them securely while providing additional features like **encryption**, **clipboard logging**, and **automatic log retrieval upon termination**.

## 🚀 Features
- **Logs keystrokes** and stores them in a file.
- **Encrypts keystroke logs** for enhanced security.
- **Records clipboard content** (copied text).
- **Auto-displays log file path upon termination**.
- **Runs in the background** without user intervention.
- **Easy log retrieval** using a simple command.

---

## 📥 Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/YourUsername/KeyloggerProject.git
```

### Step 2: Install Dependencies
```bash
pip install pynput pyperclip cryptography
```

### Step 3: Run the Keylogger
```bash
python3 keylogger.py
```

---

## 🔹 Python Implementation

### 📝 Code Structure
- `keylogger.py` → Main keylogger script
- `log_storage/` → Directory for storing logs
- `decrypt_logs.py` → Decryption script for log files

### 🏃 Running the Keylogger
```bash
python3 keylogger.py
```
Upon termination, it will display the path where logs are stored.

### 🔎 Viewing Logs
To check the logged keystrokes, run:
```bash
cat ~/.logs/keystrokes.log
```

---

## 🔐 Encryption & Security
- Logs are stored in an **encrypted format**.
- Only authorized users can **decrypt and read logs**.

### 🔑 Decrypt Logs
Use the provided script to decrypt logs:
```bash
python3 decrypt_logs.py
```

---

## 📜 License
This project is licensed under the MIT License.

## ⚠️ Disclaimer
<i>This project is for **educational purposes only**. Do not use it for unethical activities.</i>

## 🤝 Contributing
Want to improve this project? Fork the repository and submit a pull request!

## 📢 Contact
- GitHub: [Your Profile](https://github.com/YourUsername)
- Email: your@email.com
