from utils.utils import *

def getHomeData():
    movieCount = len(df['title'].values)  # 电影个数
    maxRate = df['rate'].max()  # 豆瓣最高评分
    castsList = typeList('casts')
    maxCasts = max(castsList, key=castsList.count)  # 出场最多演员  python第24
    countryList = typeList('country')
    maxCountry = max(countryList, key=countryList.count)  # 制片国家最多数
    typesList = typeList('type')
    typeCount = len(set(typesList))  # 电影种类数  python第26
    langList = typeList('lang')
    maxLang = max(langList, key=langList.count)  # 电影语言最多数

    return movieCount, maxRate, maxCasts, maxCountry, typeCount, maxLang

def getTypesEchartsData():
    typesList = typeList('type')
    typeObj = {}
    for type in typesList:
        if typeObj.get(type, -1) == -1:  # 解释在python第27
            typeObj[type] = 1
        else:
            typeObj[type] += 1

    typesEchartsData = []
    for key, value in typeObj.items():
        typesEchartsData.append({
            'name': key,
            'value': value
        })
    return typesEchartsData


def getRatesEchartsData():
    ratesList = df['rate'].map(lambda x: float(x)).values  # python-30
    ratesList.sort()  # python-29
    rateObj = {}
    for type in ratesList:
        if rateObj.get(type, -1) == -1:  # 解释在python第27
            rateObj[type] = 1
        else:
            rateObj[type] += 1
    return list(rateObj.keys()), list(rateObj.values())

def getTableData():
    tableData = df.values
    for i, item in enumerate(tableData):
        item[16] = item[16].split(',')
    return tableData



# def getMovieUrl(title):
#     movieData = df.values
#     for i in range(len(movieData)):
#         if str(movieData[i][2]) == title:
#             return movieData[i][-1]
#     return '暂无预告片！'

def getMovieUrl(title):
    movieData = df.values
    for i, item in enumerate(movieData):  # 必须用两个变量去接受enumerate
        if str(item[2]) == title:
            return item[-1]
    return '暂无预告片！'


