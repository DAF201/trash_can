
import requests
from datetime import datetime
import base64
import get_data
import download_token

def upload():
    auc = ''
    auc=base64.b64encode(auc.encode()).decode()
    url = ''
    time=str(datetime.now())
    token=download_token.get_token()
    data=get_data.processed_data()
    #this is a dict
    headers = {
        'content-type': "application/json",
        'WM_SVC.NAME': "",
        'WM_QOS.CORRELATION_ID': time,
        'WM_SEC.ACCESS_TOKEN': token,
        'Authorization': 'Basic '+auc}

    for x in data:
        put_data = requests.put(url, params={}, json={
            "sku": x,
            "quantity": {"unit": "EACH", "amount": data[x]}}, headers=headers)
    return put_data.text
    #return messages for checking
