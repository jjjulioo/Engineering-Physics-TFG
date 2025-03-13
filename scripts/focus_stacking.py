import cv2
import numpy as np
from skimage import exposure
import os
import time

# Step 1: Capture images from the DSLR webcam
def capture_images(camera_index=0, num_images=3, delay=3):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return []
    
    captured_images = []
    print("Press SPACE to capture each image.")
    
    for i in range(num_images):
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture image.")
                continue
            
            cv2.imshow("Live View", frame)
            key = cv2.waitKey(1) & 0xFF
            
            if key == 32:  # Spacebar to capture
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                captured_images.append(gray)
                print(f"Captured image {i+1}")


                #Revisar esta seccion, que yo hice para guardar las imagenes
                '''filepath = os.path.join("C:\Users\julio\OneDrive\Documents\Ingenieria Fisica\I Semestre 2025\TFG - SistemaOptico Canon 70D\screenshots\focus_stack",
                                       f"image_{i+1}")
                cv2.imwrite(filepath, gray)
                '''


                time.sleep(delay)  # Give time to adjust focus manually
                break
            elif key == 27:  # Escape key to exit
                cap.release()
                cv2.destroyAllWindows()
                return []

    cap.release()
    cv2.destroyAllWindows()
    return captured_images

# Align Images (Optional, only if the camera slightly moved)
def align_images(images):
    aligned = [images[0]]
    orb = cv2.ORB_create()
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    for i in range(1, len(images)):
        kp1, des1 = orb.detectAndCompute(images[0], None)
        kp2, des2 = orb.detectAndCompute(images[i], None)
        matches = matcher.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        matrix, _ = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)
        aligned_img = cv2.warpPerspective(images[i], matrix, (images[0].shape[1], images[0].shape[0]))
        aligned.append(aligned_img)
    
    return aligned

# Focus Stacking Function
def focus_stack(images):
    stacked = np.zeros_like(images[0], dtype=np.float32)
    laplacians = [cv2.Laplacian(img, cv2.CV_64F) for img in images]
    sharpness = np.argmax(np.abs(np.stack(laplacians)), axis=0)
    
    for i in range(len(images)):
        mask = (sharpness == i).astype(np.float32)
        stacked += mask * images[i]
    
    stacked = np.clip(stacked, 0, 255).astype(np.uint8)
    return stacked

# Main workflow
images = capture_images()
if images:
    aligned_images = align_images(images)
    stacked_image = focus_stack(aligned_images)
    
    # Save and show result
    cv2.imwrite('stacked_image.jpg', stacked_image)
    cv2.imshow('Stacked Image', stacked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No images captured. Exiting...")
