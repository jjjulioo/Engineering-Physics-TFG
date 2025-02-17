import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "C:/Users/julio/OneDrive/Documents/Ingenieria Fisica/I Semestre 2025/TFG - SistemaOptico Canon 70D/IMG_0008 - Copy.JPG"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute gradient magnitude using Sobel operator
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Plot the results
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title("a) Original Color Image")
axes[0, 0].axis("off")

axes[0, 1].imshow(gray, cmap="gray")
axes[0, 1].set_title("b) Grayscale Image")
axes[0, 1].axis("off")

axes[1, 0].imshow(gradient_magnitude, cmap="gray")
axes[1, 0].set_title("c) Gradient Magnitude Image")
axes[1, 0].axis("off")

axes[1, 1].imshow(edges, cmap="gray")
axes[1, 1].set_title("d) Edge-detected Image")
axes[1, 1].axis("off")

plt.tight_layout()
plt.show()