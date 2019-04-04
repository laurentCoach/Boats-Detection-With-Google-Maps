#Autor : Laurent Cesaro

# Resize all image in folder
# Dim 300x300

# Load library
import cv2
 
import os
import time
os.getcwd()
train = "D:/Users/S06077/Downloads/tl_data/training/JPEGImages/"

# dimension images
dim  = (300, 300) 

for i, filename in enumerate(os.listdir(train)):
    i = i + 1
    print(i)

    time.sleep(1) #if no timesleep, bug in rename file
    
    # load the image and show it
    image = cv2.imread("folder/GE_" + str(i) + ".jpg", cv2.IMREAD_COLOR)


    # perform the actual resizing of the image and show it
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
    # Save image
    cv2.imwrite('folder_target/' + str(i) + '.png', resized)
