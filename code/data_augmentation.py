"""
@author: Laurent Cesaro

Data Angmentation to multiply images in our dataset

Flip images

"""

import cv2
import numpy as np

import os
import time
os.getcwd()
train = "folder/images_augmentation/"

# dimension images
dim  = (300, 300) 

for i, filename in enumerate(os.listdir(train)):
    i = i + 1
    print(i)
    
    time.sleep(1)
    
    image = cv2.imread("folder/images_train/" + str(i) + ".png", cv2.IMREAD_COLOR)


    flipped_img = cv2.flip( image, 0 )
    
    resized = cv2.resize(flipped_img, dim, interpolation = cv2.INTER_AREA)
    
    cv2.imwrite('folder/images_augmentation/' + str(i) + '.png', resized)
