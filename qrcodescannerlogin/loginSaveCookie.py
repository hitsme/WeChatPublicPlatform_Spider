#!/usr/bin/python3
# encoding: utf-8
from selenium import webdriver
import time
import  re
import  json
from bs4 import BeautifulSoup
from dao import table_login_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from qrcodelib import qrdecode
browser=webdriver.Chrome()
browser.get("https://mp.weixin.qq.com/")
browser.maximize_window()
time.sleep(5)

browser.find_element_by_name("account").send_keys("1182681022@qq.com")
browser.find_element_by_name("password").send_keys("bingo2146295901")
browser.find_element_by_class_name("btn_login").click()
time.sleep(3)

#html=browser.find_elements_by_xpath("//*").__getattribute__("outerHTML")
html = browser.execute_script("return document.documentElement.outerHTML")
soup=BeautifulSoup(html,'lxml')
qrcodediv=soup.find_all(src=re.compile("loginqrcode"),class_="weui-desktop-qrcheck__img js_qrcode")
qrcodeurl=re.findall(r'src="(.*?)"',str(qrcodediv[0]),re.I)
#print(qrcodeurl[0])
#browser.get("https://mp.weixin.qq.com"+qrcodeurl[0])
browser.save_screenshot("qrcode.png")
time.sleep(2)

loginurlBarCode=qrdecode.deqrcode('qrcode.png')
loginurl=str(loginurlBarCode).split(',')[1].replace("'","")
print(loginurl)

engine=create_engine("mysql+mysqldb://root:hitsme52035203@localhost:3306/mysql")
Session=sessionmaker(bind=engine)
session=Session()
loginurlObj=table_login_url.login_url(
    loginurl=loginurl,
    update=time.localtime(),
    islogin=False
)
session.add(loginurlObj)
session.commit()
time.sleep(20)
logincookies=browser.get_cookies()
with open('cookies.txt', 'w') as f:
 f.write('# Netscape HTTP Cookie File\n')
 f.write('# http://curl.haxx.se/rfc/cookie_spec.html\n')
 f.write('# This is a generated file!  Do not edit.\n')
 f.write('\n')
 for item in logincookies:
    expiry=""
    try:
      expiry=str(item["expiry"])
    except:
        expiry=""
    f.write(str(item["domain"])+"	"+str(item["httpOnly"]).upper()+"	/	"+str(item["secure"]).upper()+"	"+expiry+"	"+item["name"]+"	"+item["value"]+"\n")
jsonCookies = json.dumps(logincookies)
with open('cookies.json', 'w') as f:
        f.write(jsonCookies)
print(browser.get_cookie("openid2ticket_otVyI05ehjJZxURwRA996xgvLbng"))




