import get_data
from datetime import datetime
import post_value
import get_token
import time
run_time = 1
#keep running
query = """query {
          Data
          }
}"""
url = 'http://localhost:4000/graphql'
#for quantity and sku
amount = tuple(get_data.amount())
sku = tuple(get_data.sku())
record = tuple(get_data.amount())
#manually restart this when sku changed

auc = '198996da-a477-4d55-b658-db40b7775356:AIjsJk_BmFsRFl31Ei0toy12ydI2awRLKVSTFDaKah69ZrQIOwDervn8g-xhH1q93BYPJcvujnP4R4EzZyiZa7s'
token_ur = 'https://marketplace.walmartapis.com/v3/token'
post_url = 'https://marketplace.walmartapis.com/v3/inventory'
that_token = ''
#token and post
if __name__=='__main__':
  while run_time > 0:
      try:
          now=datetime.now()
          current_time = now.strftime("%H:%M:%S")
          print("rum_time:", run_time, "||", "current_time:", current_time)
          record_update = []
          # see if the quantity changed
          if record_update != record:
              record = list(record_update)
              record = tuple(record)
              # update quantity
              if ('sku' in post_value.post(auc, sku, record, that_token, post_url)):
                              # def post( auc, sku,amount, token,     Url)
                  # see if token changed
                  print("Item(s) quantity updated")
              else:
                  that_token = get_token.token(token_ur, auc)
                                  # def token(Url,      auc)
                  post_value.post(auc, sku, record, that_token, post_url)
                  print('token update')
                  # if token changed, update token and quantity
          else:
              pass
      finally:
          time.sleep(5)
        #stop for 5 mins, and repeat
