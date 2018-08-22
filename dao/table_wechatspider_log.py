# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Time,Boolean,Text,Date
from constant import constant
engine=create_engine(constant.connectMysqlUrl, max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
                     )
Base=declarative_base()
class wechatspider_log(Base):
    __tablename__='wechatspider_log'
    wechatid=Column(String(50),primary_key=True)
    aid=Column(String(100),nullable=True)
    atitle=Column(Text,nullable=True)
    spiderdate=Column(Date,nullable=True)
    fornumname=Column(String(200),nullable=True)
    fornumid=Column(String(50),nullable=True)
    def __repr__(self):
        return '%s(%r)'%(self.__class__.__name__,self.tid)

Base.metadata.create_all(engine)