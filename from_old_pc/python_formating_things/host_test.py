import json
import requests
query = """query {
          Data
}"""
url = 'http://localhost:4000/graphql'
def get_data():
    r = requests.post(url, json={'query': query})
    json_data = json.loads(r.text)
    print(json_data)
    print(type(json_data))
get_data()