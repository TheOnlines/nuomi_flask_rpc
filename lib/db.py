#encoding:utf8
'''
数据库模型
'''
from flask import Flask

import MySQLdb

from config.config import MysqlConfig

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(MysqlConfig.Mysql_Config['name'],MysqlConfig.Mysql_Config['pwd'],MysqlConfig.Mysql_Config['host'],MysqlConfig.Mysql_Config['port'],MysqlConfig.Mysql_Config['db'])

db = SQLAlchemy(app)


class Share_users(db.Model):

    uid = db.Column(db.Integer, primary_key=True)

    link_url = db.Column(db.String(200), nullable=True)

    create_time = db.Column(db.String(11), nullable=True)

    title = db.Column(db.String(200), nullable=True)
    filesize = db.Column(db.String(200), nullable=True)
    filetype = db.Column(db.String(200), nullable=True)

    webtype = db.Column(db.Integer, nullable=False)

    def __init__(self, link_url, create_time, title,webtype,filesize,filetype):



        self.link_url = link_url

        self.create_time = create_time

        self.title = title

        self.filesize = filesize

        self.filetype = filetype

        self.webtype = webtype

class Spider(db.Model):
    __tablename__ = 'spider'
    id = db.Column(db.Integer, primary_key=True)

    pages = db.Column(db.Integer, nullable=False)

    tr = db.Column(db.Integer, nullable=False)

    def __init__(self, id,pages, tr):
        self.id = id

        self.pages = pages

        self.tr = tr



