#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from animation import image2txt
from animation import video2image
def run(txt_path):
    fileList = os.listdir(txt_path)
    for i in range(1, len(fileList)+1):         # 遍历所有的txt文件
        try:
            os.system('type ' + txt_path + '\\' + str(i) + '.txt')
            # 这里type命令是Windows下的命令，相信很多人没怎么用过，你试一下就知道，type+文件名，就可以在cmd里面显示文件内容
            os.system('cls')
            # 清屏的意思，每显示一次txt文件，就清屏，然后显示下一个txt
            # 这里还可以适当的加延时函数，如果显示的太快的话
        except:
            print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def start():
        video_path = r'C:\Users\Hitsme\Desktop\ezgif-4-01a7a321ae.mp4'
        image_path = r'G:\pycharmWorkspace\WeChatPublicPlatform_Spider\animation\image'
        txt_path = r'G:\pycharmWorkspace\WeChatPublicPlatform_Spider\animation\txt'
        #video2image.get_image(video_path, image_path)
        image2txt.image_to_txt(image_path, txt_path)
        run(txt_path)