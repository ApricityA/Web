import pandas as pd
from sqlalchemy import create_engine
import pymysql
engine = create_engine('mysql+pymysql://root:209708@localhost:3306/douban')

class DataToSql:

    def __init__(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='209708', database='douban', port=3306,
                                   charset='utf8mb4')
            sql = '''
                    create table movie(
                        id int primary key auto_increment,
                        directors varchar(255),
                        rate varchar(255),
                        title varchar(255),
                        cover varchar(255),
                        detailLink varchar(255),
                        casts varchar(888),
                        year varchar(255),
                        type varchar(255),
                        country varchar(255),
                        lang varchar(255),
                        time varchar(255),
                        moveTime varchar(255),
                        comment_len text,
                        starts varchar(255),
                        summary varchar(888),
                        comments varchar(10000),
                        imgList varchar(888),
                        movieUrl varchar(255))
                        '''

            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

        except:
            pass
    def clearData(self):
        df = pd.read_csv('./tempData.csv')
        df.dropna(inplace=True)  # 删除缺失值
        df.drop_duplicates()  # 删除重复值
        self.save_to_sql(df)

    def save_to_sql(self, df):
        df.to_sql('movie', con=engine, if_exists='replace', index=False, method='multi')


if __name__ == '__main__':
    DataToSql().clearData()