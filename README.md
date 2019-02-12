# object_detection

### Prerequisites

Install python 3.6 

Download labelImg
https://github.com/tzutalin/labelImg

### Create Pascal Voc Dataset

1 - Launch labelImg
command prompt : python labelImg.py

2 - Annotate your images

3 - Parse XML elements to create file.lst

All is clearly explained here :
https://gluon-cv.mxnet.io/build/examples_datasets/detection_custom.html#lst-label-for-gluoncv-and-mxnet

Exemple of content for 1 annotation :

1	4	5	1600	900	0	607	109	1049	688	VOC2018/JPEGImages/1.jpg

4 - Convert lst file to .rec
