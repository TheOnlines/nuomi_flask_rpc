#!/bin/sh
#停止sphinx服务，将输出重定向
#/opt/coreseek-4.1/bin/searchd -–stop >> opt/coreseek-4.1/var/searchd.log
#重新建立索引addindex ,将输出重定向
/opt/coreseek-4.1/bin/indexer addindex --rotate  >> /opt/coreseek-4.1/deltaindex.log
#将addindex合并到test1中
/opt/coreseek-4.1/bin/indexer --merge test1 addindex --rotate >> /opt/coreseek-4.1/var/deltaindex.log
#启动服务
#/opt/coreseek-4.1/bin/searchd >> /opt/coreseek-4.1/bin/var/searchd.log
