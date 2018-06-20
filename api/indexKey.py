#encoding:utf8
from flask import Blueprint

from modular import jsonrpc
from lib.check_auth import check_auth
mod = Blueprint('indexKey', __name__)
jsonrpc.register_blueprint(mod)

@jsonrpc.method('IndexKey.index',authenticated=check_auth)
def index():

    #fistPage = ["QQ表情", "博士论文", "硕士论文", "便民工具", "儿童健康"];
    fistPage = ["泄密者", "猛虫过江", "侏罗纪世界2","超时空同居","狂暴巨兽"];
    return fistPage