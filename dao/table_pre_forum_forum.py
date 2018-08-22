# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Time,Boolean,Enum
from constant import constant
engine=create_engine(constant.connectMysqlUrl, max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
                     )
Base=declarative_base()
class pre_forum_forum(Base):
    __tablename__='pre_forum_forum'
    fid=Column(Integer,primary_key=True)
    fup=Column(Integer,nullable=True)
    type=Column(Enum("group","forum","sub"),nullable=True)
    name=Column(String(50),nullable=True)
    status=Column(Integer,nullable=True)
    displayorder=Column(Integer,nullable=True)
    styleid=Column(Integer,nullable=True)
    threads=Column(Integer,nullable=True)
    posts=Column(Integer,nullable=True)
    todayposts=Column(Integer,nullable=True)
    yesterdayposts=Column(Integer,nullable=True)
    rank=Column(Integer,nullable=True)
    oldrank=Column(Integer,nullable=True)
    lastpost=Column(String(110),nullable=True,index=True)
    domain=Column(String(15),nullable=True,index=True)
    allowsmilies=Column(Integer,nullable=True,index=True)
    allowhtml=Column(Integer,nullable=True)
    allowbbcode=Column(Integer,nullable=True)
    allowmediacode=Column(Integer,nullable=True)
    allowanonymous=Column(Integer,nullable=True)
    allowpostspecial=Column(Integer,nullable=True)
    allowspecialonly=Column(Integer,nullable=True)
    allowappend=Column(Integer,nullable=True)
    alloweditrules=Column(Integer,nullable=True)
    allowfeed=Column(Integer,nullable=True)
    allowside=Column(Integer,nullable=True)
    recyclebin=Column(Integer,nullable=True)
    modnewposts=Column(Integer,nullable=True)
    jammer=Column(Integer,nullable=True)
    disablewatermark=Column(Integer,nullable=True)
    inheritedmod=Column(Integer,nullable=True)
    autoclose=Column(Integer,nullable=True)
    forumcolumns=Column(Integer,nullable=True)
    caformcolumns=Column(Integer,nullable=True)
    threadcahes=Column(Integer,nullable=True)
    alloweditpost=Column(Integer,nullable=True)
    simple=Column(Integer,nullable=True)
    modworks=Column(Integer,nullable=True)
    allowglobalstick=Column(Integer,nullable=True)
    level=Column(Integer,nullable=True)
    commoncredits=Column(Integer,nullable=True)
    archive=Column(Integer,nullable=True)
    recommend=Column(Integer,nullable=True)
    favtimes=Column(Integer,nullable=True)
    sharetimes=Column(Integer,nullable=True)
    disablethumb=Column(Integer,nullable=True)
    disablecollect=Column(Integer,nullable=True)

    def __repr__(self):
        return '%s(%r)'%(self.__class__.__name__,self.tid)

Base.metadata.create_all(engine)


