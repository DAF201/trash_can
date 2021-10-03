import requests
import base64
from datetime import date
def token(url, auc):
    auto = base64.b64encode(auc.encode()).decode()
    today_date = str(date.today())
    header = {'WM_SVC.NAME': '@sales-channel/walmart',
               'WM_QOS.CORRELATION_ID': today_date,
               'Accept': 'application/json',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Authorization': 'Basic '+auto}
    p = requests.post(
        url, params={'grant_type': "client_credentials"}, headers=header)

    token = p.json()
    token = token['access_token'].encode()
    return token