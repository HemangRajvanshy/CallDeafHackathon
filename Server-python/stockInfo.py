import sys
import requests

def getInfo(name):
    name = name.lower()
    URL = "https://www.blackrock.com/tools/hackathon/portfolio-analysis"
    company = name + '~100'
    PARAMS = {'positions' : name}
   # portfolioReq = requests.get(URL, PARAMS)
    portfolioReq = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis",
                                {
                                    'positions': company
                                })
    data = portfolioReq.json()
    #print(data)
    #print(dailyChange)
    dailyChange = data["resultMap"]['PORTFOLIOS'][0]["portfolios"][0]["returns"]["latestPerf"]["oneDay"]
    return dailyChange

#getInfo(sys.argv[1])
