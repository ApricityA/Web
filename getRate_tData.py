from utils.utils import *
# from utils import *
import re
def getRate_tData():
    typeData = list(set(typeList('type')))
    return typeData

def getAllRate_tData(type):
    if type == 'all':
        rateList = df['rate'].values
        rateList.sort()
    else:
        typeData = df['type'].map(lambda x: x.split(','))
        typeRate = df['rate'].values
        rateList = []
        for i, j in enumerate(typeData):
            if type in j:
                rateList.append(typeRate[i])
        rateList.sort()
    rateObj = {}
    for i in rateList:
        if i not in rateObj:
            rateObj[i] = 1
        else:
            rateObj[i] += 1

    return list(rateObj.keys()), list(rateObj.values())

def getSearch(searchWord):
    starts = list(df.loc[df['title'].str.contains(searchWord)]['starts'])[0].split(',')
    titles = list(df.loc[df['title'].str.contains(searchWord)]['title'])[0]
    data = [{
        'name': '五星',
        'value': 0
    },{
        'name': '四星',
        'value': 0
    },{
        'name': '三星',
        'value': 0
    },{
        'name': '二星',
        'value': 0
    },{
        'name': '一星',
        'value': 0
    }]
    for i, j in enumerate(starts):
        data[i]['value'] = float(re.sub('%', '', j))
    return data, titles

def getYearMeanData():
    year = list(df['year'].unique())
    year.sort()
    yearMean = []
    for i in year:
        yearMean.append(round(df.loc[df['year'] == i]['rate'].mean(), 1))
    return year,yearMean

