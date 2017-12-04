#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

dir = "/Users/ruixinglong/Pictures/照片图库.photoslibrary/Masters"

def copy_photo(dir, name):
    list = os.listdir(dir)
    for v in list:
        file = dir + os.path.sep + v
        if os.path.isdir(file):
            copy_photo(file, name)
        else:
            if os.path.isfile(file):
                file_arr = os.path.splitext(file)
                if file_arr[1].lower() == name:
                    print file

if __name__ == '__main__':
    copy_photo(dir, '.jpg')
