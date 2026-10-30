# 🐞 Code-debugging AI

An AI-powered debugging assistant that analyzes source code from uploaded images and helps developers identify bugs, understand errors, and generate solutions.

---

## 📌 Overview

BugFixer AI allows users to upload an image containing source code. The application extracts the code from the image and uses AI to analyze it.

Users can:

- Detect coding errors
- Get debugging hints
- Understand why the error occurs
- Generate corrected code

The goal is to make debugging faster and help developers learn from their mistakes.

---

## ✨ Features

- 📷 Upload code screenshots
- 🔍 Detect programming errors
- 💡 Generate debugging hints
- 📖 Explain detected issues
- ✅ Generate corrected code
- 🤖 AI-powered response

---

## 🛠 Tech Stack

- Python
- Streamlit
- OpenAI / Gemini API *(use whichever you used)*
- OCR (Image to Text)
- Pillow
- Requests

---

## ⚙️ Workflow

1. Upload a code image
2. Extract text from the image
3. Send extracted code to the AI model
4. Analyze the code
5. Generate:
   - Bug Detection
   - Hint
   - Explanation
   - Solution
6. Display results to the user

---

## 📂 Project Structure

```text
code_debugger/
│   └── api_call.py
│   └── app.py
├── assets/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/rakibulislam93/code-debugger-app.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```


## 🚀 Future Improvements

- Support multiple programming languages
- Improve OCR accuracy
- Detect runtime errors
- Syntax highlighting
- Chat-based debugging assistant
- VS Code extension
- FastAPI backend
- Docker deployment

---

## 👨‍💻 Author

**Md Rakibul Islam**

GitHub: https://github.com/rakibulislam93

LinkedIn: https://linkedin.com/in/rakibulislam93

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
