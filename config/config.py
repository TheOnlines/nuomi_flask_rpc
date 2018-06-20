#encoding:utf8
'''
sphinx 配置文件
'''
class SphinxConfig(object):
    Sphinx_Config = {
        'host':'127.0.0.1',
        'port': 9312,
        'db': 'pan',
        'p':15
    }
'''
mongodb 配置文件
'''
class MongoConfig(object):
    Mongo_Config = {
        'host':'47.105.45.25',
        'port': 27017,
        'db': 'pan',
        'name':"root",
        'pwd':"zhaowei123"
    }

'''
mysql 配置文件
'''
class MysqlConfig(object):
    Mysql_Config = {
        'host':'47.105.45.25',
        'port': 3306,
        'db': 'pan',
        'name':"root",
        'pwd':"zhaowei123"
    }
'''
登录证书
'''
class Credentials(object):
    Creden_Tials = {
        'zhaowei':"zhaowei123"
    }