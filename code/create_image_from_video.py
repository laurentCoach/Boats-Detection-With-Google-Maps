"""
@author: Laurent Cesaro

1 - Convert a video from youtube to mp4
"""
#https://www.youtube.com/watch?v=r2ShaMdKF6E
import cv2

    
# Video PATH
videoFile = "videoplayback.mp4"
# Read Video
vidcap = cv2.VideoCapture(videoFile)
success,image = vidcap.read()

#################### Setting up parameters ################

seconds = 1
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
multiplier = fps * seconds

#################### Initiate Process ################

while success:
    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    success, image = vidcap.read()
    
    if frameId % multiplier == 0:
        # Resize Image
        image = cv2.resize(image, (300, 300))
        # Save Image - Define path
        cv2.imwrite("screen/%d.png" % frameId, image)

vidcap.release()
print("Complete")
