import cv2
import numpy as np

#Este script permite generar una imagen binaria con el tal de trazar una diferenciacion entre las fases
#liquido-aire con el fin de poder realizar un buen aforo.

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 20, 80)


    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('sobely', edges)

    k = cv2.waitKey(5) 
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()






