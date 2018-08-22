#!/usr/bin/python3
# #-*-coding:utf-8-*-
import datetime
import time
import traceback
import uuid
from dao import table_pre_forum_post
from dao import table_pre_forum_forum
from dao import table_pre_forum_post_tableid
from dao import table_pre_forum_thread
from constant import constant
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
def getContent(atitle,alink):
    #缤纷花食，悄悄挖掘玫瑰的不同吃法[mp4]http://45.62.226.188/缤纷花食，悄悄挖掘玫瑰的不同吃法.mp4[/mp4]
    return str(atitle)+'  [href]'+alink+'[/href]'
def getTid(session):
    #session.query(table_login_url.login_url).order_by(table_login_url.login_url.id.desc()).first()
    pre_forum_postObj = session.execute("select * from pre_forum_post order by tid desc limit 0,1").first()
    return pre_forum_postObj.tid

def getFid(session,fornumname):
    try:
        pre_forum_forumObj=session.execute('select * from pre_forum_forum where name="'+fornumname+'"')
        return pre_forum_forumObj.fid
    except:
        print('function getFid() error')
def publishWebsite(aid,atitle,alink,fornumname):
    engine = create_engine(constant.connectMysqlUrl)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
      pre_forum_postObj=session.execute('select * from pre_forum_post order by pid desc limit 0,1')
      lastPid=pre_forum_postObj.pid
      lastPid+=1
      print(lastPid)
      fid=getFid(session,fornumname)
      tid=getTid(session)
      tid+=1
      timeminute=time.time()
      session.execute("""insert into pre_forum_post(pid, fid, tid,first, author,
                                                  authorid,subject,dateline,message,useip,
                                                  port,invisible,anonymous,usesig,htmlon,
                                                  bbcodeoff,smileyoff,parseurloff,attachment,rate,
                                                  ratetimes,position) 
                                                  values("%s","%s","%s","%s","%s",
                                                         "%s","%s","%s","%s","%s",
                                                         "%s","%s","%s","%s","%s",
                                                         "%s","%s","%s","%s","%s",
                                                         "%s","%s")"""
                                                  %(lastPid,fid,tid,'1','admin',
                                                    '1',atitle,str(timeminute),getContent(atitle,alink),'127.0.0.1',
                                                    '740','0','0','1','0',
                                                    '0','-1','0','0','0',
                                                    '0','1'))
      session.execute("""insert into  pre_forum_thread(tid,fid,posttableid,typeid,sortid,readperm,price,author,authorid,subject,dateline, lastpost,lastposter,views,replies,displayorder,highlight,digest,rate,special,attachment,moderated,closed,stickreply,recommends,recommend_add,recommend_sub,heats,status,isgroup,favtimes,sharetimes,stamp,icon,pushedaid,cover,replycredit) 
VALUES("%s" ,"%s", 0, 0, 0, 0, 0, 'admin', 1, "%s","%s", "%s", "admin", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,32, 0, 0, 0, -1, -1, 0, 0, 0)"""%(tid,fid,atitle,str(timeminute),str(timeminute)))
      session.execute("""insert into pre_forum_post_tableid(pid) values("%s")"""%(lastPid))
      #"UPDATE `pre_forum_forum` SET threads=threads+1, posts=posts+1,todayposts=todayposts+1 ,lastpost='" + currentPId + " " + rss.getTitle() + " " + time + " 狂飙蜗牛" + "' WHERE fid=" + fid;
      session.execute('UPDATE pre_forum_forum SET threads=threads+1, posts=posts+1,todayposts=todayposts+1 ,lastpost="' + str(lastPid) + ' ' + atitle + ' ' +str(timeminute) + ' admin' + '" WHERE fid=' + str(fid))
      writeWechatSpiderLog(aid,atitle,fid,fornumname)
      session.commit()
    except Exception as e:
      print(e)
      print ('function publishWebsite error')
    finally:
        session.close()
    return

def writeWechatSpiderLog(aid,atitle,fornumid,fornumname):
    engine = create_engine(constant.connectMysqlUrl)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        dldate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("""insert into WechatSpider_log(wechatid,aid,atitle,fornumname,fornumid,spiderdate)
 values("%s","%s","%s","%s","%s","%s")"""%(str(uuid.uuid1()),aid,atitle,fornumname,fornumid,str(dldate)))
        session.execute("""insert into WechatSpider_log(wechatid,aid,atitle,fornumname,fornumid,spiderdate)
 values("%s","%s","%s","%s","%s","%s")"""%(str(uuid.uuid1()),aid,atitle,fornumname,fornumid,str(dldate)))

        session.commit()
    except :
        traceback.print_exc()
        print ('function write WechatSpider_log error')
    finally:
        session.close()
    return