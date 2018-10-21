import sys
import requests

def getQuote(s):
    result, success = try_Ticker(s)
    if success:
        return result, success

    return try_Name(s)

def try_Name(s):
    name = ""
    if get_name(s) != None:
        name = get_name(s)[1]
        URL = "https://api.iextrading.com/1.0/stock/" + str(get_name(s)[0]) + "/delayed-quote"
    else:
        URL = "https://api.iextrading.com/1.0/stock/notastock/delayed-quote"

    return tryRun(URL, name)

def try_Ticker(s):
    URL = "https://api.iextrading.com/1.0/stock/" + s + "/delayed-quote"
    #print(URL)
    return tryRun(URL, s)

def tryRun(URL, s):
    success = True;
    response = requests.get(url = URL)
    res = "mmh"
    if response.status_code != 200:
        success = False;
        res = "failed"
    else:
        data = response.json()
        price = data['delayedPrice']
        high = data['high']
        low = data['low']
        res = s + ". Current stock price is " + str(price) + " last business day's low was " + str(low) + " and the high was " + str(high)
    return res, success

def get_name(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    symbol = symbol.lower()

    for x in result['ResultSet']['Result']:
        name = x['name'].lower()

        if name[0:4] == symbol[0:4]:
            return x['symbol'].replace(".", "-").split("-", 1)[0], x['name']


# company = get_name("Tesla")

# print(company)

# quote = getQuote(sys.argv[1])
# print(sys.argv[1] + " is currently worth: $" + str(quote) + " USD. Please note that there is a 15-minute delay on stock-quotes.")
