# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Time,Boolean
from constant import constant
engine=create_engine(constant.connectMysqlUrl, max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
                     )
Base=declarative_base()
class pre_forum_thread(Base):
    __tablename__='pre_forum_thread'
    fid=Column(Integer,nullable=True,index=True)
    tid=Column(Integer,primary_key=True)
    posttableid=Column(Integer,nullable=True)
    typeid=Column(Integer,nullable=True)
    sortid=Column(Integer,nullable=True,index=True)
    readperm=Column(Integer,nullable=True,index=True)
    price=Column(Integer,nullable=True)
    author=Column(Integer,nullable=True)
    authorid=Column(Integer,nullable=True)
    subject=Column(String(80),nullable=True,index=True)
    dateline=Column(Integer,nullable=True)
    lastposter=Column(Integer,nullable=True)
    views=Column(Integer,nullable=True)
    replies=Column(Integer,nullable=True)
    displayorder=Column(Integer,nullable=True)
    highlight=Column(Integer,nullable=True)
    digest=Column(Integer,nullable=True)
    rate=Column(Integer,nullable=True)
    special=Column(Integer,nullable=True)
    attachment=Column(Integer,nullable=True)
    moderated=Column(Integer,nullable=True)
    closed=Column(Integer,nullable=True)
    stickreply=Column(Integer,nullable=True)
    recommends=Column(Integer,nullable=True)
    recommend_add=Column(Integer,nullable=True)
    recommand_sub=Column(Integer,nullable=True)
    heats=Column(Integer,nullable=True)
    status=Column(Integer,nullable=True)
    isgroup=Column(Integer,nullable=True)
    favtimes=Column(Integer,nullable=True)
    sharetimes=Column(Integer,nullable=True)
    stamp=Column(Integer,nullable=True)
    icon=Column(Integer,nullable=True)
    pushedaid=Column(Integer,nullable=True)
    cover=Column(Integer,nullable=True)
    replycredit=Column(Integer,nullable=True)
    relatebytag=Column(Integer,nullable=True)
    maxposition=Column(Integer,nullable=True)
    bgcolor=Column(String(8),nullable=True)
    comments=Column(Integer,nullable=True)
    hidden=Column(Integer,nullable=True)

    def __repr__(self):
        return '%s(%r)'%(self.__class__.__name__,self.tid)

Base.metadata.create_all(engine)


