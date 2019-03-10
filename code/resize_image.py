#Autor : Laurent Cesaro


# Load library
import cv2
 
# load the image and show it
image = cv2.imread("image.jpg", cv2.IMREAD_COLOR)

# If print(image) == None --> problem
print(image)

r = 100.0 / image.shape[1]
# Here resize width
# Specify your dimension
# x, y
dim = (100, int(image.shape[0] * r))
#dim  = (224, 224) 

# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# Save image
cv2.imwrite('image_save.jpg', resized)

# Show image
cv2.imshow("resized", resized)
cv2.waitKey(0)
