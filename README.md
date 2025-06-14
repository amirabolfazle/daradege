# hamekare

A lightweight Python wrapper By Amirabolfazle, providing access to a variety of AI-powered tools such as:

* Image generation
* Logo and QR code creation
* Ai Response

---

## 📦 Installation

```bash
pip install hamekare
```

---

## 🚀 Usage

### 🔼 Image & Logo Tools (`genp.py`)

```python
from hamekare import genp

# Generate AI image
genp.image("a futuristic city skyline at night")

# Generate Persian logo
genp.logo("hamekare")

# Generate QR code
genp.qr("https://hamekare.ir")
```

---

### 🧠 Ai Chat (`ai.py`)

```python
from hamekare import ai

#ask llama ai model to response your prompt!
ai.llama('Hello')

#ask chatgpt ai model to response your prompt!
ai.chatgpt('Hello')

#ask deepseek ai model to response your prompt!
ai.deepseek('Hello')

#ask gemini ai model to response your prompt!
ai.gemini('Hello')

#ask llamqwena ai model to response your prompt!
ai.qwen('Hello')

#ask nemotron ai model to response your prompt!
ai.nemotron('Hello')
```

---

## 📄 License

MIT License
