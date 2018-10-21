import sys
import requests

def getQuote(s):
    URL = "https://api.iextrading.com/1.0/stock/" + s + "/delayed-quote"
    #print(URL)
    success = True;
    response = requests.get(url = URL)
    price = -1
    if response.status_code != 200:
        success = False;
    else:
        data = response.json()
        price = data['delayedPrice']
    return success, price



#quote = getQuote(sys.argv[1])
#print(sys.argv[1] + " is currently worth: $" + str(quote) + " USD. Please note that there is a 15-minute delay on stock-quotes.")
