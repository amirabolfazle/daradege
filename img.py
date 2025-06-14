def jpg(text,res):
    with open(f"{res}.jpg", "wb") as f:
        f.write(text)
    return f

def png(text,res):
    with open(f"{res}.png", "wb") as f:
        f.write(text)
    return f

def webp(text,res):
    with open(f"{res}.webp", "wb") as f:
        f.write(text)
    return f