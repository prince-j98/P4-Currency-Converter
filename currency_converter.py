# can also use urllib3 for this but requests is more convenient
# the job is to push the html page into BeautifulSoup
import requests

# bs4 helps to parse html text
from bs4 import BeautifulSoup as soup

url = "https://www.exchangerates.org.uk/Indian-Rupee-INR-currency-table.html"
page = requests.get(url)

# html parsing
content = soup(page.content, 'html.parser')

# find the container where you need to get the info from (usually under the div or tr tag)
# gets everything inside that one item
rate_col1 = content.findAll("tr", {"class":"colone"})
rate_col2 = content.findAll("tr", {"class":"coltwo"})

filename = "Currency Converter.csv"
f = open(filename, "w")

header = "Name, Rate, Symbol\n"
f.write(header)


for currency_num in range(9, len(rate_col1)):
    column = rate_col1[currency_num]

    currency_title = column.a["title"]

    rate = column.findAll("b", {})
    currency_rate = rate[1].text

    symbol = column.findAll("a", {})
    currency_symbol = symbol[1].text[4:]

    f.write(currency_title + "," + currency_rate + "," + currency_symbol + "\n")

f.write("Indian Ruppee,1,INR")
f.close()

# to do
    # extract cell wise data from excel
    # make GUI with input currency, input amount, and output currency

import csv
database = csv.reader(open("Currency Converter.csv", "r"))

csv_list = list(database)
title_list = list()
rate_list = list()
symbol_list = list()
num = 0

while num < len(csv_list):
    title_list.insert(num, csv_list[num][0])
    rate_list.insert(num, csv_list[num][1])
    symbol_list.insert(num, csv_list[num][2])
    num +=1

in_currency = input("Please enter the currency symbol you want to convert: ").upper()
in_amt = int(input("Please enter the amount you want to convert: "))
out_currency = input("Please enter the currency symbol you want to convert into: ").upper()
out_amt = 0


if symbol_list.count(in_currency) == 1:
    currency1 = rate_list[symbol_list.index(in_currency)]
else:
    print("Invalid input")

if symbol_list.count(out_currency) == 1:
    currency2 = rate_list[symbol_list.index(out_currency)]
else:
    print("Invalid input")


out_amt = round((float(currency1) * float(in_amt)) / float(currency2), 5)
print(str(in_currency) + " "+ str(in_amt) + " = " + str(out_currency) + " " + str(out_amt))