from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import datetime
import pandas as pd


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD',
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '',
}

session = Session()
session.headers.update(headers)


response = session.get(url, params=parameters)
data = json.loads(response.text)
date_time_today = datetime.date.today()

try:
  currencies = []
  for entry in data['data']:
    curency = {}
    curency["V24h"] = str(entry['quote']['USD']['volume_24h'])
    currencies.append(curency)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print("error!")


df = pd.DataFrame(currencies)

df1 = pd.read_csv("Coinmarketap.csv")
df1[f"{date_time_today}"] = df
df1.to_csv("Coinmarketap.csv", index=False)



# df.to_csv("Coinmarketap.csv")
