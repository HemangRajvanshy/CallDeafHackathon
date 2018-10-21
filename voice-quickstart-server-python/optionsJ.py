import requests
import json

def getOptions(abbreviation):
    url = "https://query1.finance.yahoo.com/v7/finance/options/" + abbreviation
    result = requests.get(url).json()
    #print(result)
    #calls = result["optionChain"]["result"][0]["calls"]
    #puts = result["optionChain"]["result"][0]["puts"]
    #print(puts)
    #print()
    #print(calls)
    calls = result["optionChain"]["result"][0]["options"][0]['calls']
    puts = result["optionChain"]["result"][0]['options'][0]['puts']
    retDict={}
    retDict['calls']=calls
    retDict['puts']=puts
    return retDict

getOptions("AAPL")

def getNearMoneyOptions(optionDict, price):
    callList=[]
    putList=[]
    for index in optionDict['calls']:
        if abs((index["strike"] - price)) < 5:
            contractDataDict={}
            contractDataDict["strike"] = index["strike"]
            contractDataDict["volume"] = index["volume"]
            contractDataDict["lastPrice"] = index["lastPrice"]
            contractDataDict["inTheMoney"] = index["inTheMoney"]
            callList.append(contractDataDict)
            #print(index)
    for otherIndex in optionDict['puts']:
        if abs((otherIndex["strike"] - price)) < 5:
            contractDataDict={}
            contractDataDict["strike"] = otherIndex["strike"]
            contractDataDict["volume"] = otherIndex["volume"]
            contractDataDict["lastPrice"] = otherIndex["lastPrice"]
            contractDataDict["inTheMoney"] = otherIndex["inTheMoney"]
            putList.append(contractDataDict)
    return callList, putList

print(getNearMoneyOptions(getOptions("AAPL"), 219))
