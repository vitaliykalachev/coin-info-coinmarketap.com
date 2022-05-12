# from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
#
# cmc = CoinMarketCapAPI('{34d5ce82-1675-480e-a2d7-fbed4053bfbe}')
#
# r = cmc.cryptocurrency_info(symbol='BTC')
#
#
#
# print(repr(r.status))
# print(repr(r.data))
# print(repr(r.credit_count))
# # do_something(r.data)
#

# from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
# from requests import Request, Session
#
# cmc = CoinMarketCapAPI('{34d5ce82-1675-480e-a2d7-fbed4053bfbe}')  # Pro environnement
# # cmc = CoinMarketCapAPI() # Sandbox environnement
#
# try:
#     r = cmc.cryptocurrency_info(symbol='BTC')
# except CoinMarketCapAPIError as e:
#     r = e.rep
#
# print(repr(r.error))
# print(repr(r.status))
# print(repr(r.data))
import pprint

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '34d5ce82-1675-480e-a2d7-fbed4053bfbe',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  pprint.pprint(data)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)