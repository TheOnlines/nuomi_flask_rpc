# -*- coding: utf-8 -*-
from flask import Blueprint

from modular import jsonrpc
from lib.db import *
from lib.sphinx import sphinx
from lib.mono import mono
from lib.db import Share_users
from lib.check_auth import check_auth
from config.config import SphinxConfig;
import math
mod = Blueprint('Search', __name__)
jsonrpc.register_blueprint(mod)
@jsonrpc.method('Search.index',authenticated=check_auth)

def index(key,p):
        resList = {}
        searchWord = sphinx().instanceof().runsphinx("id desc", p, key);
        #print searchWord
        if searchWord is None :
            resList['list'] ={'title':'没有数据了'},
            resList['nextpage'] = 'end'
            resList['total'] = 0
            return resList
        matches = searchWord['matches']
        total = searchWord['total']

        lists = []

        for i in matches:
           if len(mono().instanceof().find({'uid':i['id']})) == 0:
               try:
                   select = Share_users.query.filter_by(uid=i['id']).first()
               except:
                   continue

               if select is None:
                   continue
               mono().instanceof().add({'uid': i['id'],'link_url':select.link_url,'create_time':int(select.create_time),'title':select.title,'webtype':int(select.webtype),'filesize':select.filesize})
           lists.append(i['id'])
        listmongo =  mono().instanceof().find({"uid":{"$in":lists},"del":{"$exists":False}})
        resList['list'] = sorted(listmongo, key=lambda s: s['uid'],reverse=True)

        if int(p+1) <= math.ceil(total/SphinxConfig.Sphinx_Config['p']):
            resList['nextpage'] = int(p+1)
        else:
            resList['nextpage'] = 'end'
        resList['total'] = total
        return resList




