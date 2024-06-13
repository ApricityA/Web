from utils.query import *

def delMovie(movieName):
    sql = "DELETE FROM movie WHERE title = %s"
    query(sql, [movieName])
    return '删除成功'

def delTableData():
    sql = "select * from movie"
    data = list(query(sql, [], 'select'))
    def map_fn(item):
        item = list(item)
        item[16] = item[16].split(',')
        return item
    data = map(map_fn, data)
    return data