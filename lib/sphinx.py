#encoding:utf8
from sphinxapi import *
from config.config import SphinxConfig
'''
auther:By赵巍
sphinx 单例模式sphinx插件类  @TODO::搜索可能会出现线程锁的问题 后期修改
'''
class sphinx(object):

    #占位符填充实例化数据
    def __init__(self):
        #print SphinxConfig.Sphinx_Config['host']
        self.sphinx = SphinxClient()
        self.sphinx.SetServer(SphinxConfig.Sphinx_Config['host'], SphinxConfig.Sphinx_Config['port'])  # 主机与端口
        self.sphinx.SetWeights([100, 1])
        self.sphinx.SetMatchMode(SPH_MATCH_EXTENDED2)

    #进行数据存储
    @classmethod
    def instanceof(self):

        if not hasattr(sphinx,"_instance"):
            self._instance = self()

        return self._instance

    #获取数据
    #order: 排序
    #limit:分页
    #word : 分词关键词
    def runsphinx(self,order,limit,word):
        #print 123
        self.sphinx.SetSortMode(SPH_SORT_EXTENDED, order);
        limit = limit*SphinxConfig.Sphinx_Config['p']
        self.sphinx.SetLimits(limit, SphinxConfig.Sphinx_Config['p'])
        return self.sphinx.Query(word, '*')
#print sphinx().instanceof().runsphinx('id desc',0,'赵巍')