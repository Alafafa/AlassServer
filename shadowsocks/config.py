import logging

#Config
MYSQL_HOST = 'flit.alafafa.com'
MYSQL_PORT = 3306
MYSQL_USER = 'dbuser'
MYSQL_PASS = 'password'
MYSQL_DB = 'ss_panel'

MANAGE_PASS = 'themanagepass'
#if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
#make sure this port is idle
MANAGE_PORT = 23333

PANEL_VERSION = 'V3' # V2 or V3. V2 not support API
API_URL = 'http://panel.alafafa.com/mu'
API_PASS = 'theapipass'
NODE_ID = '21'
CHECKTIME = 60
SYNCTIME = 120

#BIND IP
#if you want bind ipv4 and ipv6 '[::]'
#if you want bind all of ipv4 if '0.0.0.0'
#if you want bind all of if only '4.4.4.4'
SS_BIND_IP = '0.0.0.0'
SS_METHOD = 'rc4-md5'

#LOG CONFIG
LOG_ENABLE = True
LOG_LEVEL = logging.DEBUG
LOG_FILE = '/var/log/shadowsocks.log'

