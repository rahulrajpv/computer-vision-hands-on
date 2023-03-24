# Importing Libraries
import numpy as np # for matrix operations
import cv2 as cv2 # for image processing

# Reading the sample image from the local drive
image = cv2.imread(r"C:\Users\rahul\OneDrive\Pictures\118644924_610960472901025_1658440095779597941_n.jpg", 0) # reading the image from the local drive and converting it to grayscale image by passing 0 as the second argument

# Resizing the image
image01 = cv2.resize(image, (500, 500)) # resizing the image to 500x500

# Applying Canny edge detection
edges = cv2.Canny(image01, 80, 100) # threshold1=80, threshold2=100

# Displaying the image
cv2.imshow("Edges", edges) # displaying the image
cv2.waitKey(0) # waiting for the user to press any key
cv2.destroyAllWindows() # destroying all the windows
