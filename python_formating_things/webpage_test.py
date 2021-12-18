from requests_html import HTMLSession
session = HTMLSession()
url = 'https://www.bilibili.com'
r = session.get(url)
print(r.html.text)