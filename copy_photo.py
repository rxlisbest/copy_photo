#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
import datetime

date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
dir = "/Users/ruixinglong/Pictures/照片图库.photoslibrary/Masters"
to_dir = "/Users/ruixinglong/Downloads/%s/" % date

def copy_file(dir, to_dir, ext):
    list = os.listdir(dir)
    for v in list:
        file = dir + os.path.sep + v
        to_file = to_dir + os.path.sep + v
        if os.path.isdir(file):
            copy_file(file, to_dir, ext)
        else:
            if os.path.isfile(file):
                file_arr = os.path.splitext(file)
                if file_arr[1].lower() == ext:
                    shutil.copyfile(file, to_file)
                    print file

def R(dir, to_dir, ext_arr):
    for ext in ext_arr:
        to_dir_inner = to_dir + os.path.sep + ext[1:]
        to_dir_exist = os.path.exists(to_dir_inner)
        if to_dir_exist == False:
            r = os.makedirs(to_dir_inner)
        copy_file(dir, to_dir_inner, ext)

if __name__ == '__main__':
    R(dir, to_dir, ['.jpg', '.mov'])
