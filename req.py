import requests

def req(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        return f"{response.status_code} | cannot give content from daradegeapi."
