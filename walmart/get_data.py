import json
import requests
query = """query {
          Data
}"""
url = 'http://localhost:4000/graphql'
def get_data():
    Raw=''
    r = requests.post(url, json={'query': query})
    json_data = json.loads(r.text)
    for x in json_data["data"]["Data"]:
        Raw=Raw+x
    Raw=Raw.split(",")
    return Raw
def sku():
    sku=get_data()
    tmp=[]
    for x in sku:
        if ('JTD') in x:
            x=x.split(":")[1]
            x=x.split(r'"')[1]
            tmp.append(x)
    return tmp
def amount():
    amount=get_data()
    tmp=[]
    for x in amount:
        if ('amount') in x:
            x=x.split(":")[1]
            x=x.split(r'"')[1]
            tmp.append(x)
    return tmp
# print(sku())
# print(amount())