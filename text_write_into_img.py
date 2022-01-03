import requests
import base64
with open('fzzl.png', 'rb')as cover:
    data = base64.b64encode(cover.read())
print(data)
re = requests.get(
    'https://via.placeholder.com/4500/000000/FFFFFF.png?text=%s' % str(data)).content
with open('test.jpg', 'wb')as file:
    file.write(re)
