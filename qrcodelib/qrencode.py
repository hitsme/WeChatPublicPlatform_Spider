import qrcode
import os
import sys
import time

def qrencode(filename,decodestr):
    QRImagePath = filename
    qr = qrcode.QRCode(
        version=1,

        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    data = decodestr
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(filename)

def openQrcodeImage(QRImagePath):
    if sys.platform.find('darwin') >= 0:
        os.system('open %s' % QRImagePath)
    elif sys.platform.find('linux') >= 0:
        os.system('xdg-open %s' % QRImagePath)
    else:
        os.system('call %s' % QRImagePath)
    print(QRImagePath)
    time.sleep(5)
    os.remove(QRImagePath)