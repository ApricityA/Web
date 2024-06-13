from pymysql import *

conn = connect(host='localhost', user='root', password='209708', database='douban', port=3306)
cursor = conn.cursor()

def query(sql, params, type='no_select'):  # sql表示SQL查询语句，params表示查询参数，type表示查询的类型，默认为’no_select’。
    params = tuple(params)  # 将params参数转换为元组类型。
    cursor.execute(sql, params)  # 使用游标对象的execute方法执行SQL查询语句。sql参数是要执行的SQL语句，params参数是查询的参数
    if type != 'no_select':
        data_list = cursor.fetchall()  # 使用游标对象的fetchall方法获取查询结果的所有行数据，并将其赋值给data_list变量,data_list是一个列表
        conn.commit()  # 提交对数据库的修改，将更改保存到数据库中
        return data_list
    else:
        conn.commit()
        return '数据库语句执行成功！'