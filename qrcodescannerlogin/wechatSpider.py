#!/usr/bin/python3
# encoding: utf-8
from http.cookiejar import MozillaCookieJar, CookieJar
from urllib.request import Request, build_opener, HTTPCookieProcessor, urlopen
import time
from tools.JsonTools import jsonString2Dict
from constant import constant
from discuz.publishDiscuzMethods import publishWebsite
from dao.table_wechatspider_log import wechatspider_log
from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker
from qrcodescannerlogin import loginSaveCookie
from animation.running import start
DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}
DEFAULT_TIMEOUT = 360


def gen_login_cookie():
    cookie = MozillaCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    return cookie

def grabContent(cookie,url):
    req = Request(url, headers=DEFAULT_HEADERS)
    opener = build_opener(HTTPCookieProcessor(cookie))
    response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    encode_json = response.read().decode("utf8")
    decode_json = jsonString2Dict(encode_json)
    return decode_json
def grab(cookie):
 engine = create_engine(constant.connectMysqlUrl)
 Session = sessionmaker(bind=engine)
 session = Session()
 spiderSql='select spiderurl,fornumname from Spider_Record where isenable="1"'
 logintokenSql='select * from login_token where isenable=true order by id desc'
 spiderlist=session.execute(spiderSql)
 logintoken=session.execute(logintokenSql).first()
 for j in spiderlist:
    requestUrl=j.spiderurl.replace(j.spiderurl[j.spiderurl.index("token="):j.spiderurl.index("&lang=zh_CN")],"token="+logintoken.token)
    #print(requestUrl)
    req = Request(requestUrl, headers=DEFAULT_HEADERS)
    opener = build_opener(HTTPCookieProcessor(cookie))
    response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    encode_json=response.read().decode("utf8")
    decode_json=jsonString2Dict(encode_json)
    print(decode_json)
    try:
        print(decode_json['app_msg_cnt'])
    except:
        loginSaveCookie.updateLoginCookie()

    endIndex=int(decode_json['app_msg_cnt'])
    time.sleep(5)
    while endIndex>=0:
      spiderUrl=requestUrl.replace('begin=0','begin='+str(endIndex))
      decode_json=grabContent(cookie,spiderUrl)
      #print(decode_json)
      for i in decode_json['app_msg_list']:
        cnt=session.query(func.count(wechatspider_log.aid)).filter(wechatspider_log.aid==i["aid"]).scalar()
        if cnt==0:
            #publishWebsite(str(i['aid']),str(i['digest']),str(i['link']),str(j[1]))
             print("文章抓取入库---"+j.fornumname+"------"+str(i['digest']))
      endIndex -= 6
      time.sleep(100)
    response.close()
    session.close()



def startspider():
    start()
    print("虫子开始觅食............................")
    cookie = gen_login_cookie()
    grab(cookie)
    cookie.save(filename='./cookies.txt',ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    #initWeChatSpiderLog()
    #initSpiderRecord()
    startspider()
    #req = Request('https://mp.weixin.qq.com', headers=DEFAULT_HEADERS)
    #opener = build_opener(HTTPCookieProcessor(gen_login_cookie()))
    #response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    #encode_json = response.read().decode("utf8")
    #print (encode_json)
