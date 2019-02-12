# object_detection

### AWS SageMaker NoteBook :
https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_amazon_algorithms/object_detection_pascalvoc_coco/object_detection_recordio_format.ipynb

### Tutorial to prepare your data 
https://gluon-cv.mxnet.io/build/examples_datasets/detection_custom.html#lst-label-for-gluoncv-and-mxnet

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

4 - Convert lst file to .rec with im2rec.py (/code). Open a terminal and write this command :

python im2rec.py --pack-label --num-thread 4 train.lst /VOC2018/JPEGImages --no-shuffle
