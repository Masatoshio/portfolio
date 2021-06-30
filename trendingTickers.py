import requests
from bs4 import BeautifulSoup
import numpy as np
from datetime import datetime

url = "https://finance.yahoo.com/trending-tickers/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
tickers = soup.find_all('td')

prices = {}
for i in range(0,360,12):
  symbol = tickers[i].text
  prices[symbol] = tickers[i+2].text

to_buy = np.random.choice(list(prices.keys()))
time = datetime.now().time()
print("Bought", to_buy, "at $", prices[to_buy], "@", time)
