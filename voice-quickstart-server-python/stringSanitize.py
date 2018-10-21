def stringClean(s):
    removeThese=["the","eh","uh","a","i","what","want","to","two","share","shares","see"]
    listOfString = s.split()
    retS = ""
    for x in range (len(listOfString)):
        listOfString[x]=listOfString[x].casefold()
        listOfString[x]=listOfString[x].strip('.')
        listOfString[x]=listOfString[x].strip(',')
        if listOfString[x] in removeThese:
            listOfString[x] = ""
        retS += listOfString[x] + " "
    return retS.strip(" ")
    
        
