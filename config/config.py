#encoding:utf8
'''
sphinx 配置文件
'''
class SphinxConfig(object):
    Sphinx_Config = {
        'host':'127.0.0.1',
        'port': 9312,
        'db': '#',
        'p':15
    }
'''
mongodb 配置文件
'''
class MongoConfig(object):
    Mongo_Config = {
        'host':'127.0.0.1',
        'port': 27017,
        'db': '#',
        'name':"#",
        'pwd':"#"
    }

'''
mysql 配置文件
'''
class MysqlConfig(object):
    Mysql_Config = {
        'host':'127.0.0.1',
        'port': 3306,
        'db': '#',
        'name':"#",
        'pwd':"#"
    }
'''
登录证书
'''
class Credentials(object):
    Creden_Tials = {
        'zhaowei':"#"
    }