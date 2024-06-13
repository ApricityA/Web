from utils.utils import *
def getMapData():
    mapList = typeList('country')
    mapObj = {}
    for j in mapList:
        if j not in mapObj:
            mapObj[j] = 1
        else:
            mapObj[j] += 1
    return list(mapObj.keys()), list(mapObj.values())

def getLangData():
    langList = typeList('lang')
    langObj = {}
    for i in langList:
        if i not in langObj:
            langObj[i] = 1
        else:
            langObj[i] += 1
    return list(langObj.keys()), list(langObj.values())