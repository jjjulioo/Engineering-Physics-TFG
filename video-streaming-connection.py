import numpy as np
import matplotlib as plt
import cv2 as cv

cap = cv.VideoCapture(1)

while True: 
    ret, frame = cap.read()

    # Get frame dimensions
    height, width, _ = frame.shape

     # Calculate the middle of the frame
    middle_x = width // 2
    middle_y = height // 2


     # Draw a red vertical line in the middle of the frame
    color = (0, 0, 255)  # Red in BGR
    thickness = 2  # Thickness of the line
    cv.line(frame, (middle_x, 0), (middle_x, height), color, thickness)
    cv.line(frame, (0, middle_y), (width, middle_y), color, thickness)

    image = np.zeros(frame.shape, np.uint8)
    
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

