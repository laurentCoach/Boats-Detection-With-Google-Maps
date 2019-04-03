# object_detection

### AWS SageMaker NoteBook :
https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_amazon_algorithms/object_detection_pascalvoc_coco/object_detection_image_json_format.ipynb

### Tutorial to prepare your data COCO DATASET
http://www.immersivelimit.com/tutorials/create-coco-annotations-from-scratch/#coco-dataset-format

### Prerequisites

Install python 3.6 

Download labelImg to annotate your images 

https://github.com/tzutalin/labelImg

### Create COCO Dataset

1 - Launch labelImg
command prompt : python labelImg.py

2 - Annotate your images

3 - Parse XML elements to create json files. One json per image.

4 - Create your s3 bucket

bucket_name
---train
   ---image.jpg 
---train_annotation
   ---image.json 
---validation
   ---val.jpg 
---validation_annotation
   ---val.json
   
5 - Load your images (jpg) and annotations (json file) in your s3

