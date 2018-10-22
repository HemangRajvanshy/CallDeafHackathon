def stringClean(s):
    removeThese=["the","eh","uh","a","i","what","want","to","two","share","shares","see","wants","not","do"]
    listOfString = s.split()
    retS = ""
    for x in range (len(listOfString)):
        listOfString[x]=listOfString[x].strip('.')
        listOfString[x]=listOfString[x].strip(',')
        listOfString[x]=listOfString[x].lower()
        if listOfString[x] in removeThese:
            listOfString[x] = ""
    listOfString = list(set(listOfString))
    for x in listOfString:
        retS += x + " "
    return retS.strip(" ")


