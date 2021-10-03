import requests
import base64
from datetime import datetime

def post(auc, sku, amount, token, Url):
#return the records from Walmart
    auto = base64.b64encode(auc.encode()).decode()
    current_time = str(datetime.now())
    headers = {
        'content-type': "application/json",
        'WM_SVC.NAME': "jtechdigital",
        'WM_QOS.CORRELATION_ID': current_time,
        'WM_SEC.ACCESS_TOKEN': token,
        'Authorization': 'Basic '+auto}
    for x in sku:
        count=0
        r = requests.put(Url, params={}, json={
            "sku": x,
            "quantity": {"unit": "EACH", "amount": amount[count]}}, headers=headers)
        count=count+1
    
    return r.text