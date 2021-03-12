import pymongo
import sys
# print(sys.path)
sys.path.append('..')
from config import mongo_host,mongo_port,mongo_db_name,mongo_db_collection_kugou, \
    mongo_db_collection_kuwo,mongo_db_collection_qq,mongo_db_collection_wangyi
# from .. import config

class MyMongodb(object):
    """
    数据清洗、存储
    """
    host = ''
    port = ''
    dbname = ''
    __post_wangyi = None
    def __init__(self):
        self.__class__.host = mongo_host
        self.__class__.port = mongo_port
        self.__class__.dbname = mongo_db_name
        # 连接mongodb
        client = pymongo.MongoClient(host=self.__class__.host ,port=self.__class__.port)
        # 打开、创建指定数据库、表
        mydb = client[self.__class__.dbname]
        self.__post_kuwo = mydb[mongo_db_collection_kuwo]
        self.__post_kugou = mydb[mongo_db_collection_kugou]
        self.__post_qq = mydb[mongo_db_collection_qq]
        self.__post_wangyi = mydb[mongo_db_collection_wangyi]

    def post_wangyi(self, item):
        # 插入到数据库
        self.__post_wangyi.insert(dict(item)) 


    def post_qq(self, item):
        # 插入到数据库
        self.__post_qq.insert(dict(item))


    def post_kugou(self, item):
        # 插入到数据库
        self.__post_kugou.insert(dict(item)) 


    def post_kuwo(self, item):
        # 插入到数据库
        self.__post_kuwo.insert(dict(item)) 


if __name__ == '__main__':
    mydb = MyMongodb()
    test = {'name':'22','age':'33','oo':'pp'}
    mydb.post_wangyi(test)
    



