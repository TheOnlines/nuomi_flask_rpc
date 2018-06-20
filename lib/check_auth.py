#encoding:utf8
from config.config import Credentials
'''
登录证书类
'''
def check_auth(username, password):
    #return True

    try:
        if not Credentials.Creden_Tials.has_key(username):
            return False

        if Credentials.Creden_Tials[username] != password :
            print Credentials.Creden_Tials[username]
            return False
        return True
    except:
        return False