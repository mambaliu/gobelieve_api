# -*- coding: utf-8 -*-

DEBUG=False

REDIS_HOST="10.168.188.86"
REDIS_PORT=6380
REDIS_DB=0
REDIS_PASSWORD=""

MYSQL_HOST = "rdsme36vin2uqrn.mysql.rds.aliyuncs.com"
MYSQL_PORT = 3306
MYSQL_AUTOCOMMIT = True
MYSQL_CHARSET = 'utf8'

MYSQL_USER = "gobelieve"
MYSQL_PASSWD = "123456"


MYSQL_IM_DATABASE = "gobelieve"
MYSQL_GB_DATABASE = "gobelieve"


# host,port,user,password,db,auto_commit,charset
MYSQL_IM = (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_IM_DATABASE, MYSQL_AUTOCOMMIT, MYSQL_CHARSET)

MYSQL = (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_GB_DATABASE, MYSQL_AUTOCOMMIT, MYSQL_CHARSET)


FS_HOST="10.168.188.86"
FS_PORT=18888

IM_RPC_URL = "http://10.168.188.86:7777"

MICROSOFT_CLIENTID = 'leisi'
MICROSOFT_CLIENT_SECRET = 're2QgKJvsHSW9M5LMelScVVuyEW/RmL6UR9sAMgRpFk='

GOOGLE_API_KEY = "AIzaSyCN5ebuj46zfoOTM1SGsRJ1uinc5M8xYoQ"
SOCKS5_PROXY = 'socks5://127.0.0.1:1080'
