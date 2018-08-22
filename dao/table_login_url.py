# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Time,Boolean
from constant import constant
engine=create_engine(constant.connectMysqlUrl)
Base=declarative_base()
class login_url(Base):
    __tablename__='login_url'
    id=Column(Integer,primary_key=True)
    loginurl=Column(String(200),nullable=False,index=True)
    update=Column(Time,nullable=False)
    islogin=Column(Boolean,nullable=False,index=True)
    def __repr__(self):
        return '%s(%r)'%(self.__class__.__name__,self.loginurl)

Base.metadata.create_all(engine)


