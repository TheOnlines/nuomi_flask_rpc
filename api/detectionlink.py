#encoding:utf8
from flask import Blueprint

from modular import jsonrpc
from lib.check_auth import check_auth
mod = Blueprint('detectionlink', __name__)
jsonrpc.register_blueprint(mod)
import urllib2,sys
from lib.mono import mono
import random
defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

from bs4 import BeautifulSoup

@jsonrpc.method('Detectionlink.index',authenticated=check_auth)

def index(uid,url):

    #代理ip池
    iplist = []
    try:

        for i in mono().instanceof().findall({},"proxyip"):
            iplist.append(i['ip'])
        ip = random.sample(iplist,1)

        httpproxy_handler = urllib2.ProxyHandler({"http":"http://%s"%(ip[0])})
        nullproxy_handler = urllib2.ProxyHandler({})

        proxySwitch = True

        if proxySwitch:
            opener = urllib2.build_opener(httpproxy_handler)
        else:
            opener = urllib2.build_opener(nullproxy_handler)

        urllib2.install_opener(opener)

    except :

        return [2]

    try:
        the_page = urllib2.urlopen(url,timeout=4).read()


        soup = BeautifulSoup(the_page,"html.parser")

        urlstatus = 0

        if soup.title.text == "页面不存在" or soup.title.text == "百度网盘-链接不存在" :
            mono().instanceof().update({'del':4},{'uid':int(uid)})
            urlstatus = 1


    except Exception as e:

        urlstatus = 2

    return [urlstatus]