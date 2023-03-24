#importing libraries


import cv2

# Load the image in grayscale
img = cv2.imread("C:\Users\rahul\OneDrive\Pictures\sample01.jpg.jpg", 0) #

# parameters needed for corner detetion 
max_corners = 100000000 # maximum number of corners to detect
quality_level = 0.001 # minimum quality of corner
min_distance = 1 # minimum euclidean distance between corners

# Apply Shi-Tomasi corner detection
corners = cv2.goodFeaturesToTrack(img, max_corners, quality_level, min_distance) # detect corners

# Convert corners to integers
corners = corners.astype(int) # convert to integers

# Draw circles at the corners
for corner in corners: # for each corner
    x, y = corner.ravel() # get the x and y coordinates
    cv2.circle(img, (x, y), 1, (255, 0, 0), -1) # draw a circle at the corner

# Display the corners in the image
cv2_imshow(img) #
