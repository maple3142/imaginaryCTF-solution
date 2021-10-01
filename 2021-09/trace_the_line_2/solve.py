import requests
from bs4 import BeautifulSoup
from hashlib import md5

url = "http://puzzler7.imaginaryctf.org:13337"
path = "/"
i = 0
while True:
    print(url + path, md5(str(i).encode()).hexdigest())
    resp = requests.get(url + path)
    soup = BeautifulSoup(resp.text, "html.parser")
    try:
        print(soup.select_one("div[style]").text)
        path = soup.select_one("form")["action"]
    except:
        print(resp.text)
    i += 1
