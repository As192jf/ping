import requests

url = 'http://recipe-inline.onrender.com/'

x = requests.post(url)

print(x.text)
