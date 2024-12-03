import numpy as np
import matplotlib as plt
import cv2 as cv
print("OpenCV version:", cv.__version__)

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
