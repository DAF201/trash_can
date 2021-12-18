import requests
from datetime import date
import time
from datetime import datetime
import base64

def token(Url, auc):
    auto = base64.b64encode(auc.encode()).decode()
    Date = str(date.today())
    headers = {'WM_SVC.NAME': '@sales-channel/walmart',
               'WM_QOS.CORRELATION_ID': Date,
               'Accept': 'application/json',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Authorization': 'Basic '+auto}
    p = requests.post(
        Url, params={'grant_type': "client_credentials"}, headers=headers)

    token = p.json()
    token = token['access_token'].encode()
    return token
def post(auc, sku, amount, token, Url):

    auto = base64.b64encode(auc.encode()).decode()
    current_time = str(int(time.time()))
    headers = {
        'content-type': "application/json",
        'WM_SVC.NAME': "jtechdigital",
        'WM_QOS.CORRELATION_ID': current_time,
        'WM_SEC.ACCESS_TOKEN': token,
        'Authorization': 'Basic '+auto}
    for x in sku:
        r = requests.put(Url, params={}, json={
            "sku": x,
            "quantity": {"unit": "EACH", "amount": amount}}, headers=headers)
    
    return r.text
run_time = 1
auc = '198996da-a477-4d55-b658-db40b7775356:AIjsJk_BmFsRFl31Ei0toy12ydI2awRLKVSTFDaKah69ZrQIOwDervn8g-xhH1q93BYPJcvujnP4R4EzZyiZa7s'
token_ur = 'https://marketplace.walmartapis.com/v3/token'
post_url = 'https://marketplace.walmartapis.com/v3/inventory'
that_token = ''
sku = { 'JTD-300',
        'JTD-1358',
        'JTD-386',
        'JTD-677',
        'JTD-617'}
amount = 8
while run_time > 0:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("RumTime:", run_time, "||", "current_time:", current_time)
    run_time = run_time+1
    if('sku'in post(auc, sku, amount, that_token, post_url)):
        print('token success')
    else:
        that_token=token(token_ur, auc)
        print('token update')