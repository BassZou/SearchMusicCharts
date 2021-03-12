import pymongo

class MyMongodb(object):
    """
    数据清洗、存储
    """
    mongo_host = '127.0.0.1'
    mongo_port = 27017
    mongo_db_name = 'douyin_music'
    mongo_db_collection = 'ranking'
    __db_coll = None
    def __init__(self):
        self.__class__.host = MyMongodb.mongo_host
        self.__class__.port = MyMongodb.mongo_port
        self.__class__.dbname = MyMongodb.mongo_db_name
        # 连接mongodb
        client = pymongo.MongoClient(host=self.__class__.host ,port=self.__class__.port)
        # 打开、创建指定数据库、表
        mydb = client[self.__class__.dbname]
        self.__db_coll = mydb[MyMongodb.mongo_db_collection]


    def post(self, item):
        # 插入到数据库
        self.__db_coll.insert(dict(item)) 


    def queryall(self, args):
        return self.__db_coll.find({},projection=args)
        