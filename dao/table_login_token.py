# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Time,Boolean
from constant import constant
engine=create_engine(constant.connectMysqlUrl, max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
                     )
Base=declarative_base()
class login_token(Base):
    __tablename__='login_token'
    id=Column(Integer,primary_key=True)
    token=Column(String(100),nullable=False,index=True)
    logindate=Column(Time,nullable=False)
    isEnable=Column(Boolean,nullable=False,index=True)
    def __repr__(self):
        return '%s(%r)'%(self.__class__.__name__,self.token)

Base.metadata.create_all(engine)


