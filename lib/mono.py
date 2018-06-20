#encoding:utf8
import pymongo
from config.config import MongoConfig
'''
auther:By赵巍
sphinx 单例模式mogodb插件类
'''
class mono(object):
    #连接mongodb
    def __init__(self):
        self.connect= pymongo.MongoClient('mongodb://{0}:{1}/'.format(MongoConfig.Mongo_Config['host'],MongoConfig.Mongo_Config['port']))
        self.mongo = self.connect[MongoConfig.Mongo_Config['db']]
        self.mongo.authenticate(MongoConfig.Mongo_Config['name'], MongoConfig.Mongo_Config['pwd'])

    #进行数据存储
    @classmethod
    def instanceof(self):
        if not hasattr("mono","_instance"):
            self._instance = self()
        return self._instance

    #获取数据
    #surface: 操作的表 默认为test
    #fiter 要查询的条件
    def find(self,fiter={},surface = 'share_data'):
        #print self.mongo[surface].find(fiter, {'_id':0 }).sort({'_id':-1})
        try:

            list = []
            for i in self.mongo[surface].find(fiter, {'_id':0 }):
                i['ext'] = 'file'

                title = i['title'].split('.')
                if len(title) >1:
                    i['ext'] = title[-1]

                list.append(i)
            return list

        except:

            return False

        finally:
            self.connect.close()


    # 增
    #surface: 操作的表 默认为test
    #data 新增的数据
    def add(self, data={}, surface='share_data'):
        try:
            self.mongo[surface].insert(data)
            return True
        except:
            return False
        finally:
            self.connect.close()

    # 删
    #surface: 操作的表 默认为test
    #data 新增的数据
    def delete(self, fiter={}, surface='share_data'):

        if not fiter:
            return "条件不能为空1";
        else:
            try:
                data = self.mongo[surface].find_one(fiter)
                if not data:
                    return False
                else:
                    return self.mongo[surface].remove(data['_id'])
            except:
                return False
            finally:
                self.connect.close()

#print mono().instanceof().find({'uid':111111})
