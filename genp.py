import img
import req

# genp.logo('Sunset')
def logo(prompt):
    """**this function make a logo with your prompt! use like this:** ```genp.logo('sun')``` **and result is** ```logo.jpg``` **!**"""
    prompt = prompt.replace(' ','%20')
    return img.jpg(req.req(f"https://api.daradege.ir/logo?text={prompt}").content,"logo")

# genp.image('Sunrise')
def image(prompt):
    """**this function make a logo with your prompt! use like this:** ```genp.image('sun')``` **and result is** ```image.jpg``` **!**"""
    prompt = prompt.replace(' ','%20')
    return img.jpg(req.req(f"https://api.daradege.ir/image?text={prompt}").content,"image")
    
# genp.qr('Hello World')
def qr(text):
    """**this function make a logo with your prompt! use like this:** ```genp.qr('sun')``` **and result is** ```qr.jpg``` **!**"""
    text = text.replace(' ','%20')
    return img.jpg(req.req(f"https://api.daradege.ir/qrcode?text={text}").content,"qr")