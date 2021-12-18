import requests
re = requests.post(
    'https://fybgame.top:8000/web-1.0.0/bilibili/search?cid=311661670&match=%E5%A5%BD&av=502193304&p=1').text
print(re)
# cid: str
# character: str
# av: str
# p: str
# url = ('https://fybgame.top:8000/web-1.0.0/bilibili/search?cid=%s&match=%s&av=%s&p=%s',
#        (cid, character, av, p))
