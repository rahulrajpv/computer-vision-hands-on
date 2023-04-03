#importing libraries
import cv2
import numpy as np

#reading the sample images 
sample = cv2.imread(r"C:\Users\rahul\OneDrive\Pictures\sample01.jpg",0) #reading the sample image

#resizing the sample image
sample = cv2.resize(sample, (500, 500))

# Setting the parameters for the Shi-Tomasi corner detection
max_corners = 100000000 #maximum number of corners to be detected in the image 
quality_level = 0.001 #minimum quality of the corners to be detected
min_distance = 1 #minimum distance between the corners to be detected 

# Apply Shi-Tomasi corner detection
corners = cv2.goodFeaturesToTrack(sample, max_corners, quality_level, min_distance)

# Convert corners to integers
corners = corners.astype(int) #converting the corners to integer

# Draw circles at the corners
for corner in corners: #looping through the corners
    x, y = corner.ravel() #ravel() function is used to convert the corners to 1D array 
    cv2.circle(sample, (x, y), 1, (255, 0, 0), -1) #drawing the circles at the corners of the image 
    
# Display the corners
cv2.imshow("Corners",sample) #displaying the corners image
cv2.waitKey(0) #waiting for the user to press any key
cv2.destroyAllWindows() #destroying all the windows
