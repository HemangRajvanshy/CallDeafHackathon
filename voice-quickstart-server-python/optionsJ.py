import requests
import json

def getOptions(abbreviation):
    url = "https://query1.finance.yahoo.com/v7/finance/options/" + abbreviation
    result = requests.get(url).json()
    calls = result["optionChain"]["result"][0]["options"][0]['calls']
    puts = result["optionChain"]["result"][0]['options'][0]['puts']
    retDict={}
    retDict['calls']=calls
    retDict['puts']=puts
    return retDict

#getOptions("AAPL")

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

#print(getNearMoneyOptions(getOptions("AAPL"), 219))

def generateOptionsString(callList, putList):
    statementString = ""
    statementString = "Your near the money call options are as follows."
    for x in callList:
        if (x['inTheMoney']):
            statementString += "This option is an in the money "
        else:
            statementString += "This option is an out of the money "

        statementString += "option with a strike price of" + str(x['strike']) + "dollars. It is worth " + str(x['lastPrice']) + " dollars. " + "This has traded at a volume of" + str(x['volume']) + "."
    for x in putList:
        if (x['inTheMoney']):
            statementString += "This option is an in the money "
        else:
            statementString += "This option is an out of the money "

        statementString += "option with a strike price of" + str(x['strike']) + "dollars. It is worth " + str(x['lastPrice']) + " dollars. " + "This has traded at a volume of" + str(x['volume']) + "."
    return statementString


#callList, putList = getNearMoneyOptions(getOptions("AAPL"), 219)
#print(callList)
#print(putList)
#print(generateOptionsString(callList,putList))
#generateOptionsString(getNearMoneyOptions("AAPL", 219))

