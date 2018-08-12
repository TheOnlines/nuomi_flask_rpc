#encoding:utf8
from bs4 import BeautifulSoup
import urllib2
import time
import socket
import random
import re,sys
from multiprocessing import Process
from lib.db import *



class spiders(object):

    # 数据库修改数据
    def updateDb(self,pages,tr):

        select = Spider.query.filter(Spider.id==1).first()

        select.pages = pages

        select.tr = tr

        db.session.commit()

    # 数据库查询数据
    def selDb(self):
        select = Spider.query.first()
        return select
            #Process(target=self,args=(i,))

def spider(i):
    data = ""
    Url = "http://www.xiaoxiongaini.com/?paged="+str(i)
    #print Url;continue
    request = urllib2.Request(Url)
    request.add_header('User-agent', 'Internet Explorer')
    response = urllib2.urlopen(request).read()
    # print response;return ;
    soup = BeautifulSoup(response, 'lxml')

    #基层
    pagepub = soup.find_all(attrs={'class': 'status-publish'})
    print i
    #增量记录
    spiders().updateDb(i,len(pagepub))
    for i in pagepub:
        page = i.find_all(attrs={'class': 'entry-summary'})
        title = i.find_all(attrs={'class': 'entry-header'})

        if len(page) > 0:
            #pass;
            title =  title[0].find_all(attrs={'rel': 'bookmark'})[0].string
        else:
            continue;
        if len(page[0].find_all(attrs={'rel': 'noopener'})) > 0:
            url =  page[0].find_all(attrs={'rel': 'noopener'})[-1:][0].get('href')
        else:
            continue


        strs = page[0].find_all("p")[-1].get_text()

        regex = re.compile('\s+')

        if len(regex.split(strs)) >1:
            if len(regex.split(strs)[1].split("："))>1:
                data = regex.split(strs)[1].split("：")[1]

        t = time.time()

        share = Share_users(link_url=url,create_time=t,title=title,filesize = data,filetype=2,webtype=2)
        try:
            db.session.add(share)
        except:
            db.session.rollback()
        finally:
            db.session.commit()
if __name__ =="__main__":

    reload(sys)
    sys.setdefaultencoding('utf8')
    Url = "http://www.xiaoxiongaini.com/"
    request = urllib2.Request(Url)
    request.add_header('User-agent', 'Internet Explorer')
    response = urllib2.urlopen(request).read()
    # print response;return ;
    soup = BeautifulSoup(response, 'lxml')
    page = soup.find_all(attrs={'class': 'pagenum'})[0].string

    pagetotal = page.split('/')[1];

    #print pagetotal; exit();
    breaks = int(pagetotal)-845+2
    #print range(1, breaks);exit()
    for i in range(1, ):
        p  = Process(target=spider,args=(i,))
        p.start()
        p.join()
    print "end";

    #print spiders().selDb().tr


