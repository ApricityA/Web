from utils.utils import *
import json
import sys
sys.path.append('..')  # 引入根目录的文件如wordCloud
from wordcloud import *
import wordClouds
def getCommentsImages(searchWord):
    searchName = list(df.loc[df['title'].str.contains(searchWord)]['title'])
    # if len(searchName) == 0:
    #     return '没有找到相关电影信息。'
    # else:
    searchName = searchName[0]
    comments = df.loc[df['title'] == searchName]['comments'].values[0]
    comments = json.loads(comments)
    resSrc = wordClouds.getImages(comments)
    return resSrc, searchName