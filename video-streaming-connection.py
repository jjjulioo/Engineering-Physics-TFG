import numpy as np
import matplotlib as plt
import cv2 as cv
import os

# Specify the folder to save screenshots
save_folder = "screenshots"
os.makedirs(save_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Initialize variables for run number and suffix
run_number = 1
suffix = 'A'

cap = cv.VideoCapture(0)

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

    key = cv.waitKey(1)

    if key == ord('q'):  # Quit the program
        break
    elif key == ord('s'):  # Save screenshot
        # Define the filename dynamically
        filename = f"Run-{run_number}{suffix}.png"
        filepath = os.path.join(save_folder, filename)

        # Save the image
        cv.imwrite(filepath, frame)
        print(f"Screenshot saved: {filepath}")
    elif key == ord('n'):  # Move to the next run (increment run number)
        run_number += 1
        suffix = 'A'  # Reset suffix to 'A'
        print(f"Moved to Run-{run_number}{suffix}")
    elif key == ord('a'):  # Change suffix
        suffix = chr(ord(suffix) + 1)  # Increment suffix alphabetically
        print(f"Updated to Run-{run_number}{suffix}")
    
cap.release()
cv.destroyAllWindows()



