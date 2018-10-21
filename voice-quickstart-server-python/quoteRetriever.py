import sys
import requests

def getQuote(s):
    success, price = try_Ticker(s)
    if success:
        return success, price

    success, price = try_Name(s)

def try_Name(s):
    URL = "https://api.iextrading.com/1.0/stock/" + get_name(s) + "/delayed-quote"
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

def try_Ticker(s):
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

def get_name(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    symbol = symbol.lower()

    for x in result['ResultSet']['Result']:
        name = x['name'].lower()

        if name[0:4] == symbol[0:4]:
            return x['symbol'].replace(".", "-").split("-", 1)[0]


company = get_name("international")

print(company)

#quote = getQuote(sys.argv[1])
#print(sys.argv[1] + " is currently worth: $" + str(quote) + " USD. Please note that there is a 15-minute delay on stock-quotes.")
