import requests
from requests.auth import HTTPDigestAuth
import json
ip="192.168.1.220"
r=requests.get("http://%s/set_output?rtmp_enable=1"%ip, auth=HTTPDigestAuth("admin","admin"))
# r=requests.get("http://www.google.com")
print(r.json)