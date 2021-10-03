import requests
import json
# this part pretend get data and organizanize data
query = """query {
          characters {
            results {
              name
              gender
            }
          }
}"""
url = 'https://rickandmortyapi.com/graphql/'
def get_data():
#return the sku(pretend) in tuple
  name_list=[]
  r = requests.post(url, json={'query': query})
  json_data = json.loads(r.text)
  for x in json_data['data']['characters']['results']:
    name_list.append(x['name'])
  name_list=tuple(name_list)
  print(name_list)
  return name_list

def get_quality():
#return the quantity(pretend) in tuple
    quality=[]
    r = requests.post(url, json={'query': query})
    json_data = json.loads(r.text)
    for x in json_data['data']['characters']['results']:
        quality.append(x['gender'])
    quality=tuple(quality)
    print(quality)
    return quality