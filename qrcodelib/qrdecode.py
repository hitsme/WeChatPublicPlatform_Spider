import os
import logging
from PIL import Image
import zxing
import random
logger = logging.getLogger(__name__)
if not logger.handlers: logging.basicConfig(level=logging.INFO)
DEBUG = (logging.getLevelName(logger.getEffectiveLevel()) == 'DEBUG')


def deqrcode(filename):
  #在当前目录生成临时文件，规避Java的路径问题
  img=Image.open(filename)
  ran=int(random.random()*100000)
  img.save('%s%s.png'%(os.path.basename(filename).split('.')[0],ran))
  zx=zxing.BarCodeReader()
  data=''
  zxdata=zx.decode('%s%s.png'%(os.path.basename(filename).split('.')[0],ran))

  os.remove('%s%s.png'%(os.path.basename(filename).split('.')[0],ran))

  if zxdata:
      logger.debug(u'识别二维码：%s%s'%(filename,zxdata))
      data=zxdata
  else:
      logger.error(u'识别二维码出错：%s'%(filename))
      img.save('%s-zxing.png'%filename)
  return data

#filename=r"G:\pycharmWorkspace\WeChatAdminPlatformSpider\WeChatAdminPlatformSpider\qrcodeScanner\qrcode.png"
#ltext=deqrcode(filename)
#print(str(ltext).split(',')[1].replace("'",""))