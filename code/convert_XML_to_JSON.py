# Laurent Cesaro
# Data Preparation (COCO DATASET) to use object detection with AWS SageMaker


# https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_amazon_algorithms/object_detection_pascalvoc_coco/object_detection_recordio_format.ipynb
# https://gluon-cv.mxnet.io/build/examples_datasets/detection_custom.html#lst-label-for-gluoncv-and-mxnet

#Parse XML elements to JSON
    
# import library
from bs4 import BeautifulSoup
import os


path, dirs, files = next(os.walk("ship_detector/train_annotation/"))
file_count = len(files)
print(file_count)


width = 300 #IMG width
height = 300 #IMG Height

# tab to store coordinates


#str_labels_c = []
    
for i in range(0, file_count):
#for i in range(1, file_count+1):
    xmin_tab = []
    ymin_tab = []
    xmax_tab = []
    ymax_tab = []
    # open & read files
    infile = open("ship_detector/train_annotation/"+str(i)+".xml","r") 
    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')

    # PARSE Elements
    width = soup.find_all('width')
    """
    for width in width:
        width = int(width.get_text())
    height = soup.find_all('height')
    for height in height:
        height = int(height.get_text())
    """
    class_id = soup.find_all('segmented')
    print(class_id)
    for class_id in class_id:
        class_id = int(class_id.get_text())
    xmin = soup.find_all('xmin')
    for xmin in xmin:
        xmin = int(xmin.get_text())
        xmin_tab.append(xmin)
    ymin = soup.find_all('ymin')
    for ymin in ymin:
        ymin = int(ymin.get_text())
        ymin_tab.append(ymin)
    xmax = soup.find_all('xmax')
    for xmax in xmax:
        xmax = int(xmax.get_text())
        xmax_tab.append(xmax)
    ymax = soup.find_all('ymax')
    for ymax in ymax:
        ymax = int(ymax.get_text())
        ymax_tab.append(ymax)
        
    name = str(i)
    if len(xmin_tab) > 1:
        annotation_tab = []
        annotation = """{"class_id": 0, "top": %s, "left": %s, "width": %s, "height": %s},"""
        categories_tab = []
        categories = """{"class_id": 1, "name": "boat"}, """
        for i in range(len(xmin_tab)):
            # Compute x, y, width, heght
            top = ymin_tab[i]
            left = xmin_tab[i]
            width = xmax_tab[i] - xmin_tab[i]
            height = ymax_tab[i] - ymin_tab[i]
            annotation = """{"class_id": 0, "top": %s, "left": %s, "width": %s, "height": %s},""" % (top, left, width, height)
            annotation_tab.append(annotation)
            
            categories_tab.append(categories)
            
        # remove last comma in last annotation_tab index
        last_index =  annotation_tab[-1:] # select last index
        annotation_tab = annotation_tab[:-1] # remove last index from list
        last_index = str(last_index) # convert to string
        last_index = last_index.replace("[","") # remove specific elements
        last_index = last_index.replace("]","") # remove specific elements
        last_index = last_index[:-2] # remove 2 last characters
        last_index = last_index[1:]  # remove first characters
        annotation_tab.append(last_index) # insert last_index without last comma
        
        # remove last comma in last categories_tab index
        last_index_cat =  categories_tab[-1:] # select last index
        categories_tab = categories_tab[:-1] # remove last index from list
        last_index_cat = str(last_index_cat) # convert to string
        last_index_cat = last_index_cat.replace("[","") # remove specific elements
        last_index_cat = last_index_cat.replace("]","") # remove specific elements
        last_index_cat = last_index_cat[:-3] # remove 2 last characters
        last_index_cat = last_index_cat[1:]  # remove 2 first characters
        categories_tab.append(last_index_cat) # insert last_index without last comma

        annotation_str = ' '.join(annotation_tab)
        categories_str = ' '.join(categories_tab)
        data = """{"file": "%s", "image_size": [{"width": 300, "height": 300, "depth": 3}], 
                "annotations": [
                %s], 
                "categories": [
                    %s]}""" % (name, annotation_str, categories_str)
   
    else:     
        # Compute x, y, width, heght
        top = ymin
        left = xmin
        width = xmax - xmin
        height = ymax - ymin   
        
        data = """{"file": "%s", "image_size": [{"width": 300, "height": 300, "depth": 3}], 
                "annotations": [
                {"class_id": 0, "top": %s, "left": %s, "width": %s, "height": %s}], 
                "categories": [
                    {"class_id": 1, "name": "boat"}]}""" % (name, top, left, width, height)
        #json_data = json.dumps(data)
        print("parse data ok")
    
    name_file = "ship_detector/train_annotation/"+name+".json"
    with open(name_file, 'w') as outfile:
        outfile.write(data)
        
