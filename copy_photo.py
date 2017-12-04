#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil

dir = "/Users/ruixinglong/Pictures/照片图库.photoslibrary/Masters"
to_dir = '/Users/ruixinglong/Downloads/R/'

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

def R(dir, to_dir, ext):
    to_dir = to_dir + os.path.sep + 'R' + ext
    to_dir_exist = os.path.exists(to_dir)
    if to_dir_exist == False:
        r = os.makedirs(to_dir)
    copy_file(dir, to_dir, ext)

if __name__ == '__main__':
    R(dir, to_dir, '.jpg')
    R(dir, to_dir, '.mov')
