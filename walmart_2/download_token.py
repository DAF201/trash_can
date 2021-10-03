import requests
import base64
from datetime import date

def get_token():
    auc = ''
    auc=base64.b64encode(auc.encode()).decode()
    Today=str(date.today())
    url = ''
    header = {  'WM_SVC.NAME': '@sales-channel/walmart',
                'WM_QOS.CORRELATION_ID': Today,
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic '+auc}
    #infomation for requst
    token = requests.post(
        url, params={'grant_type': "client_credentials"}, headers=header)
    token=token.json()
    token = token['access_token'].encode()
    #get token
    #print(token)
    return token