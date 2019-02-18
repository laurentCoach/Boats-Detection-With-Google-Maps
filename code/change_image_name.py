#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:14:27 2019

@author: laurent

Change image name in folder
"""

import os
import time
os.getcwd()
train = "VOC2018/image_train/"
val = "VOC2018/image_val/"

for i, filename in enumerate(os.listdir(val)):
    i = i + 269
    print(i)

    os.rename("VOC2018/image_val/" + filename, "VOC2018/image_val/" + str(i) + ".jpg")
    time.sleep(1) #if no timesleep, bug in rename file