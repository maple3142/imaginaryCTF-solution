import httpx
from subprocess import check_output, DEVNULL

cli = httpx.Client(base_url='http://puzzler7.imaginaryctf.org:4009/', follow_redirects=False)
cli.post('/login', data={
    'user': 'forsakenChamois79215',
    'pass': 'aaaa'
})
# while True:
#     tok = cli.get('/earn').text.split('pow) solve ')[1].split('\n')[0]
#     print(tok)
#     sol = check_output(['python', 'pow.py', 'solve', tok], stderr=DEVNULL).decode()
#     print(sol)
#     r = cli.post('/earn', data={
#         'solution': sol
#     })
#     print(r.text)
#     r = cli.post('/contribute', data={
#         'amount': 1
#     })
#     print(r.text)
print(cli.get('/flag').text)
# ictf{purchased_with_blood_sweat_and_t3ars}
