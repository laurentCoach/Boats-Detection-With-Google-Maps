# Laurent Cesaro
# Data Preparation to use object detection with AWS SageMaker


# https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_amazon_algorithms/object_detection_pascalvoc_coco/object_detection_recordio_format.ipynb
# https://gluon-cv.mxnet.io/build/examples_datasets/detection_custom.html#lst-label-for-gluoncv-and-mxnet


# Parse element from xml file to create a file .lst
    
# import library
from bs4 import BeautifulSoup
import os

path, dirs, files = next(os.walk("VOC2018/Annotations/"))
file_count = len(files)-1
print(file_count)

A = 4 #Lenght of the header, at least 2
B = 5 #Lenght of the label object
C = 1600 #IMG Lenght
D = 900 #IMG Height

str_labels_c = []
    
for i in range(1, file_count+1):
    # open & read files
    infile = open("VOC2018/Annotations/"+str(i)+".xml","r") 
    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')

    # PARSE Elements
    width = soup.find_all('width')
    for width in width:
        width = int(width.get_text())
    height = soup.find_all('height')
    for height in height:
        height = int(height.get_text())
    
    class_id = soup.find_all('segmented')
    for class_id in class_id:
        class_id = str(class_id.get_text())
    xmin = soup.find_all('xmin')
    for xmin in xmin:
        xmin = str(xmin.get_text())
    ymin = soup.find_all('ymin')
    for ymin in ymin:
        ymin = str(ymin.get_text())
    xmax = soup.find_all('xmax')
    for xmax in xmax:
        xmax = str(xmax.get_text())
    ymax = soup.find_all('ymax')
    for ymax in ymax:
        ymax = str(ymax.get_text())
    
    print("parse data ok")
    str_idx = [str(i)] #ID

    # IMG path
    str_path = ["VOC2018/JPEGImages/"+str(i)+".jpg"]
    str_header = [str(A),str(B),str(C),str(D)]
    #str_labels = str(i) +'    '+ str(A) +'    '+ str(B) +'    '+ class_id +'    '+ xmin +'    '+ ymin +'    '+ xmax +'    '+ ymax +'    '+str_path
    #str_labels =  class_id +'    '+ xmin +'    '+ ymin +'    '+ xmax +'    '+ ymax
    str_labels =  [class_id,xmin,ymin,xmax,ymax]
    
    line = '\t'.join(str_idx + str_header + str_labels + str_path)
    str_labels_c.append(line)


# Write LST File    
with open('train.lst', 'w') as f:
    for item in str_labels_c:
        print("ok")
        f.write("%s\n" % item)
        