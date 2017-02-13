from googlefinance import getQuotes
import json

def getPrice(stock, name):
    price = (getQuotes(stock)[0])['LastTradeWithCurrency']
    print ("The current value of " + name +" stock is: ", AAPL)

AAPL =(getQuotes('AAPL')[0])['LastTradeWithCurrency']

print ("The current value of Apple stock is: ", AAPL)

print (json.dumps(getQuotes('AAPL'), indent=2))
print (json.dumps(getQuotes(['AAPL', 'VIE:BKS']), indent=2))

