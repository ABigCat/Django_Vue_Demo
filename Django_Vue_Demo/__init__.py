# coding=utf-8
import pymysql
pymysql.install_as_MySQLdb()
# Django连接MySQL时默认使用MySQLdb驱动，但MySQLdb不支持Python3，因此这里将MySQL驱动设置为pymysql。