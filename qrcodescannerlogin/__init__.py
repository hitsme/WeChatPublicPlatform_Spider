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
from sqlalchemy import func
engine = create_engine(constant.connectMysqlUrl)
Session = sessionmaker(bind=engine)
session = Session()
spiderSql = 'select count(*) as cnt from login_url '
spiderlist = session.query(func.count(table_login_url.login_url.id)).filter(table_login_url.login_url.id==2).scalar()
print(spiderlist)