#encoding=utf-8
'''

Mongo ACTION CLASS
'''

import pymongo
from pymongo import MongoClient

class DBAction:
    conn = None
    servers = "mongodb://localhost:27017"
    db_name = ""
    coll_name = ""
    data = []
    find_data = None

    #建立连接
    def __init__(self):
        self.conn = MongoClient(self.servers)
        print self.conn.server_info()
        databases = self.conn.database_names()
        print databases
    #释放连接
    def close(self):
        return self.conn.close()
    #DB name setting
    def db_name(self, name):
        self.db_name = name
    #删除库
    def dropDB(self):
        self.conn.drop_database(self.db_name)
    #建立表
    def createTable(self,collection):

        self.coll_name = self.conn[self.db_name][collection]
    #插入数据
    def insertDatas(self, dataArray):
        self.data = dataArray
        self.coll_name.insert(dataArray)
    #更改数据

    '''只修改最后一条匹配到的数据
           第3个参数设置为True,没找到该数据就添加一条
           第4个参数设置为True,有多条记录就不更新
    '''

    def updateData(self, findData, editData, bool1 = False, bool2 = False):
        self.coll_name.insert(findData, editData, bool1, bool2)
    #查询数据 + sort
    def queryData(self, findData, sortData = ""):
        self.find_data = self.coll_name.find(findData).sort(sortData)
        # return self.find_data(findData)
    #
    # def sortData(self, sortData):
    #     self.find_data.sort(sortData)

    #打印数据
    def printResult(self):
        for row in self.find_data:
            for key in row.keys():  # 遍历字典
                print row[key],  # 加, 不换行打印
            print ''
    #删除数据
    def deleteData(self, removeData):
        self.coll_name.remove(removeData)

