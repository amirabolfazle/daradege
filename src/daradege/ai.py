import req

# ai.llama('Hello')
def llama(prompt):
    """**this function make a chat with your prompt! use like this:** ```ai.llama('Hello')``` **and result is Like This:** ```Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?``` **!**"""
    response = req.req(f"https://api.daradege.ir/llama?text={prompt}".replace(" ", "%20"))
    return response.json()['text']

# ai.llama('Hello')
def llama(prompt):
    """**this function make a chat with your prompt! use like this:** ```ai.llama('Hello')``` **and result is Like This:** ```Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?``` **!**"""
    response = req.req(f"https://api.daradege.ir/llama?text={prompt}".replace(" ", "%20"))
    return response.json()['text']

# ai.chatgpt('Hello')
def chatgpt(prompt):
    """**this function make a chat with your prompt! use like this:** ```ai.chatgpt('Hello')``` **and result is Like This:** ```Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?``` **!**"""
    response = req.req(f"https://api.daradege.ir/ai?text={prompt}".replace(" ", "%20"))
    return response.json()['text']

# ai.deepseek('Hello')
def deepseek(prompt):
    """**this function make a chat with your prompt! use like this:** ```ai.deepseek('Hello')``` **and result is Like This:** ```Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?``` **!**"""
    response = req.req(f"https://api.daradege.ir/deepseek?text={prompt}".replace(" ", "%20"))
    return response.json()['text']

# ai.gemini('Hello')
def gemini(prompt):
    """**this function make a chat with your prompt! use like this:** ```ai.gemini('Hello')``` **and result is Like This:** ```Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?``` **!**"""
    response = req.req(f"https://api.daradege.ir/gemini?text={prompt}".replace(" ", "%20"))
    return response.json()['text']

# ai.qwen('Hello')
def qwen(prompt):
    """**this function make a chat with your prompt! use like this:** ```ai.qwen('Hello')``` **and result is Like This:** ```Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?``` **!**"""
    response = req.req(f"https://api.daradege.ir/qwen?text={prompt}".replace(" ", "%20"))
    return response.json()['text']

# ai.nemotron('Hello')
def nemotron(prompt):
    """**this function make a chat with your prompt! use like this:** ```ai.nemotron('Hello')``` **and result is Like This:** ```Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?``` **!**"""
    response = req.req(f"https://api.daradege.ir/nemotron?text={prompt}".replace(" ", "%20"))
    return response.json()['text']