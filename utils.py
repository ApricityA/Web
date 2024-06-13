import pandas as pd
from sqlalchemy import create_engine

conn = create_engine('mysql+pymysql://root:209708@localhost:3306/douban')

df = pd.read_sql('select * from movie', con=conn)

def typeList(type):
    type = df[type].values
    type = list(map(lambda x: x.split(',') if ',' in x else x.split('/'), type))  # python笔记第23
    typeList = []
    for i in type:
        for j in i:
            typeList.append(j)
    return typeList



