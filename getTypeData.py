from utils.utils import *
def getTypeData():
    typeData = typeList('type')
    dataObj = {}
    for i in typeData:
        if i not in dataObj:
            dataObj[i] = 1
        else:
            dataObj[i] += 1
    Datalist = []
    for i, j in dataObj.items():
        Datalist.append({
            'name': i,
            'value': j
        })
    return Datalist