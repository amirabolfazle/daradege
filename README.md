# daradege

A lightweight Python wrapper for [Daradege.ir](https://daradege.ir), providing access to a variety of AI-powered tools such as:

* Image generation
* Logo and QR code creation

---

## 📦 Installation

```bash
pip install daradege
```

---

## 🚀 Usage

### 🔼 Image & Logo Tools (`genp.py`)

```python
from daradege import genp

# Generate AI image
genp.image("a futuristic city skyline at night")

# Generate Persian logo
genp.logo("daradege")

# Generate QR code
genp.qr("https://daradege.ir")
```

---

### 🧠 Ai Chat (`ai.py`)

```python
from daradege import ai

ai.llama('Hello')
ai.llama('Hello')
ai.chatgpt('Hello')
ai.deepseek('Hello')
ai.gemini('Hello')
ai.qwen('Hello')
ai.nemotron('Hello')
```

---

## 📄 License

MIT License
