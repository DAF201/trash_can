import json
import requests

query = """query {
          Data
}"""
#gql formating

url = 'http://localhost:4000/graphql'
#http://(ip of mechine running the server):4000/graphql,when running non-local test

def get_data():
    Raw=''
    r = requests.post(url, json={'query': query})
    json_data = json.loads(r.text)
    for x in json_data["data"]["Data"]:
        Raw=Raw+x
    Raw=Raw.split(",")
    return Raw
#get raw data from graphql server, json form-->slicing and reforming in to String from
def sku():
    sku=get_data()
    tmp=[]
    for x in sku:
        if ('') in x:
            x=x.split(":")[1]
            x=x.split(r'"')[1]
            tmp.append(x)
    return tmp
#processing raw data
def amount():
    amount=get_data()
    tmp=[]
    for x in amount:
        if ('amount') in x:
            x=x.split(":")[1]
            x=x.split(r'"')[1]
            tmp.append(x)
    return tmp
#processing raw data
def processed_data():
    data_iterator =zip(sku(),amount())
    data=dict(data_iterator)
    return data
#combinding processed data