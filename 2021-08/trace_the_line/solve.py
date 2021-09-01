import requests
from bs4 import BeautifulSoup

url = "http://puzzler7.imaginaryctf.org:7000"
path = "/af2ee0ba6c4ec49794df61df9ccdd4e2"
while True:
    print(url + path)
    resp = requests.get(url + path)
    soup = BeautifulSoup(resp.text, "html.parser")
    try:
        print(soup.select_one("div[style]").text)
        path = soup.select_one("form")["action"]
    except:
        print(resp.text)

# ictf{7h3r3-r3@lly-1s-@-l1n3!!!}
