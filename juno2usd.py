# Script to convert Juno download link from Pound to USD

import requests
from bs4 import BeautifulSoup
from decimal import Decimal

request1 = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=USD')
content = request1.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "uccResultAmount"})
exrate = element.text
print("Current exchange rate from Pound to US Dollar is {}. (Reference:: www.xe.com)".format(exrate))
print('\n')
print("Please paste below the www.JunoDownload.com URL.")
user_url = input() #JunoDownload URL
request = requests.get(user_url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "price"})
str_price = element.text
price_without_symbol = str_price[1:] #without the pound symbol
value = float(price_without_symbol) * float(exrate)
# value = Decimal()
output = round(value,2)
print('\n')
print("This music release would cost approximately ${} USD.".format(output))