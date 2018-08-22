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
from constant import constant
from dao import table_login_token
def updateLoginCookie():
    browser = webdriver.Chrome()
    browser.get(constant.SeleniumUrl)
    browser.maximize_window()
    time.sleep(5)

    browser.find_element_by_name("account").send_keys(constant.loginAccount)
    browser.find_element_by_name("password").send_keys(constant.loginPassword)
    browser.find_element_by_class_name("btn_login").click()
    time.sleep(3)

    # html=browser.find_elements_by_xpath("//*").__getattribute__("outerHTML")
    html = browser.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html, 'lxml')
    qrcodediv = soup.find_all(src=re.compile("loginqrcode"), class_="weui-desktop-qrcheck__img js_qrcode")
    qrcodeurl = re.findall(r'src="(.*?)"', str(qrcodediv[0]), re.I)
    # print(qrcodeurl[0])
    # browser.get("https://mp.weixin.qq.com"+qrcodeurl[0])
    browser.save_screenshot("qrcode.png")
    time.sleep(2)

    loginurlBarCode = qrdecode.deqrcode('qrcode.png')
    loginurl = str(loginurlBarCode).split(',')[1].replace("'", "")
    print(loginurl)

    engine = create_engine(constant.connectMysqlUrl)
    Session = sessionmaker(bind=engine)
    session = Session()
    loginurlObj = table_login_url.login_url(
        loginurl=loginurl,
        update=time.localtime(),
        islogin=False
    )
    session.add(loginurlObj)
    session.commit()
    time.sleep(1)
    while True:
        loginurlObj = session.query(table_login_url.login_url).order_by(table_login_url.login_url.id.desc()).first()
        if loginurlObj.islogin:
            # sleep a wait,wait url scrape
            token_url_str = str(browser.current_url)
            print(token_url_str)
            logintokenObj = table_login_token.login_token(
                id=loginurlObj.id,
                token=token_url_str[token_url_str.index("token=") + 6:],
                logindate=time.localtime(),
                isEnable=True

            )
            session.add(logintokenObj)
            session.commit()
            break
        # session.refresh(loginurlObj)
        # session.expire(loginurlObj,"islogin")
        session.commit()
    logincookies = browser.get_cookies()
    with open('cookies.txt', 'w') as f:
        f.write(constant.NetScapeHeaderOne)
        f.write(constant.NetScapeHeaderTwo)
        f.write(constant.NetScapeHeaderThree)
        f.write('\n')
        for item in logincookies:
            expiry = ""
            try:
                expiry = str(item["expiry"])
            except:
                expiry = ""

            if str(item["name"]) == "pgv_pvi" or str(item["name"]) == "pgv_si":
                httpOnlyValue = "TRUE"
                secureValue = "FALSE"
            else:
                httpOnlyValue = "FALSE"
                secureValue = "TRUE"
            f.write(
                str(item["domain"]) + "	" + httpOnlyValue + "	/	" + secureValue + "	" + expiry + "	" +
                item["name"] + "	" + item["value"] + "\n")
    jsonCookies = json.dumps(logincookies)
    with open('cookies.json', 'w') as f:
        f.write(jsonCookies)






