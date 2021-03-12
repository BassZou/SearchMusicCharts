from craw.douyin_music import rgBang,ycBang,bsBang,cleanData
from db.mongodb import MyMongodb
from config import mongo_host,mongo_port,mongo_db_name,mongo_db_collection_kugou, \
    mongo_db_collection_kuwo,mongo_db_collection_qq,mongo_db_collection_wangyi

def start():
    mydb = MyMongodb()
    test = {'name':'22','age':'33','oo':'pp'}
    mydb.post_wangyi(test)

if __name__ == '__main__':
    start()