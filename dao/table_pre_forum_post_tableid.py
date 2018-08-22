# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer
from constant import constant
engine=create_engine(constant.connectMysqlUrl, max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
                     )
Base=declarative_base()
class pre_forum_post_tableid(Base):
    __tablename__='pre_forum_post_tableid'
    pid=Column(Integer,primary_key=True)

    def __repr__(self):
        return '%s(%r)'%(self.__class__.__name__,self.tid)

Base.metadata.create_all(engine)


