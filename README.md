# Object Detector with AWS Sagemaker COCO Dataset

### AWS SageMaker NoteBook :
https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_amazon_algorithms/object_detection_pascalvoc_coco/object_detection_image_json_format.ipynb

### Tutorial to prepare your data COCO DATASET
http://www.immersivelimit.com/tutorials/create-coco-annotations-from-scratch/#coco-dataset-format

### Prerequisites

Install python 3.6 

Download labelImg to annotate your images 

https://github.com/tzutalin/labelImg or http://tzutalin.github.io/labelImg/

### Images
Image size : 300 or 512

### Annotate your images
Annotate your images with labelImg.

All annotations are in XML format. You need to convert your XML to JSON. (Code : https://github.com/laurentCoach/Boats-Detection-With-Google-Maps/blob/master/code/convert_XML_to_JSON.py)

The annotation file must have the same name as the corresponding image.

### S3 storage
In AWS create a bucket in s3 to store your JPG images and your annotations.

bucket_name

- ---train

   - ---image.jpg 
   
---train_annotation

   ---image.json 
   
---validation

   ---val.jpg 
   
---validation_annotation

   ---val.json

### AWS Sagemaker
Create an instance with a notebook : https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_amazon_algorithms/object_detection_pascalvoc_coco/object_detection_image_json_format.ipynb

Train your model !

### Results
![Image of Yaktocat](https://github.com/laurentCoach/Boats-Detection-With-Google-Maps/blob/master/img/plot2.png)
