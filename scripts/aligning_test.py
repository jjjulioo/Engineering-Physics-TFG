import cv2
import numpy as np

def check_alignment(image1, image2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(image1, None)
    kp2, des2 = orb.detectAndCompute(image2, None)
    
    if des1 is None or des2 is None:
        return False  # No keypoints found
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    
    if len(matches) < 10:  # Very few matches indicate possible misalignment
        return True  # Alignment needed
    
    # Calculate mean distance between matched keypoints
    distances = [m.distance for m in matches]
    avg_distance = sum(distances) / len(distances)
    
    return avg_distance > 5  # If average distance is high, alignment is needed

# Example usage:
# Assuming `images` is your list of grayscale images
needs_alignment = any(check_alignment(images[0], img) for img in images[1:])
print("Alignment needed:", needs_alignment)