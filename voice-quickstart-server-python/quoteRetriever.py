import sys
import requests

def getQuote(s):
    URL = "https://api.iextrading.com/1.0/stock/" + s + "/delayed-quote"
    response = requests.get(url = URL)
    data = response.json()
    price = data['delayedPrice']
    return price

#quote = getQuote(sys.argv[1])
#print(sys.argv[1] + " is currently worth: $" + str(quote) + " USD. Please note that there is a 15-minute delay on stock-quotes.")
