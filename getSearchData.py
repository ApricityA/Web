from utils.utils import *

def getMovieByTitle(title):
    searchData = df.values
    resultData = []
    for i, item in enumerate(searchData):
        if str(item[2]) == title:
            item[16] = item[16].split(',')
            resultData.append(item)
    return  resultData

def getSearchData(keys):
    searchData = df.values
    resultData = []
    for i, item in enumerate(searchData):
        if item[2].find(keys) != -1:
            item[16] = item[16].split(',')
            resultData.append(item)
    return resultData