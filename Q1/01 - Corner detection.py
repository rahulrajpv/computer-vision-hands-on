import cv2

# Load the image in grayscale
img = cv2.imread("C:\Users\rahul\OneDrive\Pictures\sample01.jpg.jpg", 0)

# parameters needed for corner detetion -
max_corners = 100000000
quality_level = 0.001
min_distance = 1

# Apply Shi-Tomasi corner detection
corners = cv2.goodFeaturesToTrack(img, max_corners, quality_level, min_distance)

# Convert corners to integers
corners = corners.astype(int)

# Draw circles at the corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 1, (255, 0, 0), -1)

# Display the corners
cv2_imshow(img)
