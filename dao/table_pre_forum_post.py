# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Time,Boolean
from constant import constant
engine=create_engine(constant.connectMysqlUrl, max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
                     )
Base=declarative_base()
class pre_forum_post(Base):
    __tablename__='pre_forum_post'
    pid=Column(Integer,index=True)
    fid=Column(Integer,nullable=True,index=True)
    tid=Column(Integer,primary_key=True)
    first=Column(Integer,nullable=True)
    author=Column(String(15),nullable=True)
    authorid=Column(Integer,nullable=True)
    subject=Column(String(80),nullable=True)
    dateline=Column(Integer,nullable=True)
    message=Column(Integer,nullable=True)
    useip=Column(String(15),nullable=True)
    port=Column(Integer,nullable=True)
    invisible=Column(Integer,nullable=True)
    anonymous=Column(Integer,nullable=True)
    usesig=Column(Integer,nullable=True)
    htmlon=Column(Integer,nullable=True)
    bbcodeoff=Column(Integer,nullable=True)
    smileyoff=Column(Integer,nullable=True)
    parseurloff=Column(Integer,nullable=True)
    attachment=Column(Integer,nullable=True)
    rate=Column(Integer,nullable=True)
    ratetimes=Column(Integer,nullable=True)
    status=Column(Integer,nullable=True)
    tags=Column(String(255),nullable=True)
    comment=Column(Integer,nullable=True)
    replycredit=Column(Integer,nullable=True)
    position=Column(Integer,nullable=True)
    def __repr__(self):
        return '%s(%r)'%(self.__class__.__name__,self.tid)

Base.metadata.create_all(engine)


