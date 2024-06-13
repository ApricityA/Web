from utils.utils import *


# from utils import *
def getTime_tData():
    dataList = list(df['time'].map(lambda x: int(x[:4])))
    dataList.sort()
    dataObj = {}
    for i in range(len(dataList)):
        if dataList[i] not in dataObj:
            dataObj[dataList[i]] = 1
        else:
            dataObj[dataList[i]] += 1
    return list(dataObj.keys()), list(dataObj.values())


def getMovieTimeData():
    dataList = list(df['moveTime'])
    dataObj = [{
        'name': '短片',
        'value': 0
    }, {
        'name': '中片',
        'value': 0
    }, {
        'name': '长片',
        'value': 0
    }, {
        'name': '特长片',
        'value': 0
    }]
    for i in dataList:
        if int(i) <= 60:
            dataObj[0]['value'] = dataObj[0]['value'] + 1
        elif int(i) <= 120:
            dataObj[1]['value'] = dataObj[1]['value'] + 1
        elif int(i) <= 180:
            dataObj[2]['value'] = dataObj[2]['value'] + 1
        else:
            dataObj[3]['value'] = dataObj[3]['value'] + 1
    return dataObj
