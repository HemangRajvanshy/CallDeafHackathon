import sys
import requests
import json

def getTicker(name):
    with open('convertcsv.json') as js:
        data = json.load(js)
        for x in range(len(data)):
            company_name = data[x]['Name']
            if (name == company_name[:len(name)]):
                return data[x]["Ticker"]

ticker = getTicker(sys.argv[1])
print(ticker)
