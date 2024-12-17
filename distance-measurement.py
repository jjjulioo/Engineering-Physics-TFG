import cv2
import numpy as np

# List to store clicked points
points = []

def select_points(event, x, y, flags, param):
    """Callback function to capture mouse clicks."""
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))  # Add clicked point
        print(f"Point selected: ({x}, {y})")


# Load the image
image_path = "screenshots\Run-1A.png"  # Replace with your image path
image = cv2.imread(image_path)
clone = image.copy()  # Keep a copy for visualization

# Set up the window and mouse callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", select_points)

print("1. Click on two points to define the scale.")
print("2. Click on two points to measure a distance.")
print("Press 'q' when you are done.")

while True:
    # Draw the selected points and lines
    for i in range(len(points)):
        cv2.circle(clone, points[i], 5, (0, 0, 255), -1)  # Draw points
    if len(points) >= 2:
        cv2.line(clone, points[0], points[1], (0, 255, 0), 2)  # Scale line
    if len(points) == 4:
        cv2.line(clone, points[2], points[3], (255, 0, 0), 2)  # Measured line

    cv2.imshow("Image", clone)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):  # Exit when 'q' is pressed
        break

cv2.destroyAllWindows()

# Ensure enough points are selected
if len(points) < 4:
    print("You need to select four points: two for scale and two for measurement.")
    exit()

# Calculate the scale
def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

scale_pixel_distance = euclidean_distance(points[0], points[1])
known_physical_distance = float(input("Enter the known physical distance (e.g., in cm): "))

# Calculate pixels per unit (e.g., pixels per cm)
pixels_per_unit = scale_pixel_distance / known_physical_distance
print(f"Scale: {pixels_per_unit:.2f} pixels per unit.")

# Measure the distance between the second pair of points
measurement_pixel_distance = euclidean_distance(points[2], points[3])
physical_distance = measurement_pixel_distance / pixels_per_unit

print(f"Measured pixel distance: {measurement_pixel_distance:.2f} pixels")
print(f"Measured physical distance: {physical_distance:.2f} units")