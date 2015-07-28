# Import Libraries
import numpy as np
import cv2

# Define variables
framerate = 20.0   # frames per second
videolength = 3    # length of video in seconds

# Grab Camera
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('myvideo.avi',fourcc, framerate, (640,480))

# Video part
for i in range(int(videolength*framerate)):
    if(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)
            out.write(frame)
        else:
            continue

# Release the camera and video file
cap.release()
out.release()
