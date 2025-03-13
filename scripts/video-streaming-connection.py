import numpy as np
import matplotlib as plt
import cv2 as cv
import os
import time

# Specify the folders to save screenshots
save_folder_dslr = "screenshots/dslr"
save_folder_webcam = "screenshots/webcam"
os.makedirs(save_folder_dslr, exist_ok=True)  # Create DSLR folder if it doesn't exist
os.makedirs(save_folder_webcam, exist_ok=True)  # Create Webcam folder if it doesn't exist

# Initialize cameras (0 for webcam, 1 for DSLR if connected via USB)
webcam = cv.VideoCapture(0)  # Webcam
canon = cv.VideoCapture(1)   # DSLR Camera

time.sleep(2)

# Counter for DSLR captures
dslr_run_number = 1  # Run number
suffix = 'A'  # Capture suffix
def capture_and_save_image(camera, filename, folder):
    """Capture an image from a given camera and save it."""
    ret, frame = camera.read()
    if ret:
        filepath = os.path.join(folder, filename)
        cv.imwrite(filepath, frame)
        print(f"Screenshot saved: {filepath}")
    else:
        print("Failed to capture image.")

while True:
    ret1, frame1 = webcam.read()
    ret2, frame2 = canon.read()

    if ret1:
        # Draw crosshairs on the webcam feed
        height, width, _ = frame1.shape
        middle_x, middle_y = width // 2, height // 2
        color, thickness = (0, 0, 255), 2
        cv.line(frame1, (middle_x, 0), (middle_x, height), color, thickness)
        cv.line(frame1, (0, middle_y), (width, middle_y), color, thickness)
        cv.imshow('Webcam', frame1)
    
    if ret2:
        cv.imshow('Canon DSLR', frame2)

    key = cv.waitKey(1)
    if key == ord('q'):  # Quit program
        break
    elif key == ord('s'):  # Capture from both cameras simultaneously
        volume = input("Enter volume (cc): ")  # User inputs the volume value
        if ret2:
            dslr_filename = f"{dslr_run_number}_{suffix}_{volume}.png"
            capture_and_save_image(canon, dslr_filename, save_folder_dslr)
        if ret1:
            webcam_filename = f"{dslr_run_number}_{suffix}_{volume}_webcam.png"  # Match DSLR number
            capture_and_save_image(webcam, webcam_filename, save_folder_webcam)
        suffix = chr(ord(suffix) + 1) if suffix < 'Z' else 'A'  # Increment suffix
    elif key == ord('n'):  # Move to the next run
        dslr_run_number += 1
        suffix = 'A'  # Reset suffix
        print(f"Moved to Run-{dslr_run_number}{suffix}")

webcam.release()
canon.release()
cv.destroyAllWindows()
