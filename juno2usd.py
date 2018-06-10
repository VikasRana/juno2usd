# Script to convert Juno download link from Pound to USD

import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=USD') #exchange rate
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "uccResultAmount"})
exrate = element.text
print("Current exchange rate from GBP to USD is {}. (Reference:: www.xe.com)".format(exrate))
print('\n')

#Juno part from lines below
print("Please paste below the www.JunoDownload.com URL and press ENTER.")
user_url = input() #JunoDownload URL
request = requests.get(user_url)
content = request.content
soup = BeautifulSoup(content, "html.parser")

element = soup.find("span", {"class": "price"})
str_price = element.text

# Final calculation, I'm bad at Mathematics. Python do it for me pls!!
print('\n')
print('Found release price -> {} GBP.'.format(str_price))
price_without_symbol = str_price[1:] # without the GBP symbol
value = float(price_without_symbol) * float(exrate)
output = round(value,2) # rounds the decimal to place 2
print('\n')
print("The 320 KB/S release would cost approximately -> ${} USD.".format(output))
