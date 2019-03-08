#Autor : Laurent Cesaro


# Load library
import cv2
 
# load the image and show it
image = cv2.imread("image.jpg")

r = 100.0 / image.shape[1]
# Here resize width
dim = (100, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)