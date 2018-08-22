#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy
def image_to_txt(image_path, txt_path):
    txt_count = 1                                   # 用于命名txt文件
    fileList = os.listdir(image_path)               # 返回所有图片名称，是个字符串列表
    for file in fileList:                           # 遍历每一张图片
        img = Image.open(image_path + '\\'+ file).convert('L')
        # 这里使用到PIL库convert函数，将RGB图片转化为灰度图，参数'L'代表转化为灰度图
        charWidth = 140
        # 这个是设置你后面在cmd里面显示内容的窗口大小，请根据自己的情况，适当调整值
        img = img.resize((charWidth, 40))
        target_width, target_height = img.size
        data = numpy.array(img)[:target_height, :target_width]
        # 使用numpy库，将图像转化为数组
        with open(txt_path + '\\' + str(txt_count) + '.txt', 'w', encoding='utf-8') as f:
            txt_count += 1                      # 一张图对应一个txt文件，所以每遍历一张图，该值加一
            for row in data:
                for pixel in row:
                    if pixel < 127:             # 如果灰度值小于127，也就是偏黑的，就写一个字符 '*'
                        f.write('*')
                    else:
                        f.write(' ')
                f.write('\n')