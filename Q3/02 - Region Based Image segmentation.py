#Importing Libraries
import numpy as np 
import cv2 as cv2

# Read the input image
img = cv2.imread(r"D:\MTECH\PROJECT\CV\ASSIGNMENT\REPOSITORY\computer-vision-hands-on\Q5\dataset\Sample03.jpg")


# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detector
edges = cv2.Canny(gray, 100, 200) # 100 and 200 are the thresholds for the hysteresis procedure and gray is the input image

# Display the resulting image
cv2.imshow("edges",edges) # for image display

# Apply binary thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) #gray is the image to be thresholded, 150 is the threshold value, 255 is the max value, cv2.THRESH_BINARY is the thresholding type

# Display the resulting image
cv2.imshow("Region based",thresh) #thresh is the image to be displayed
cv2.waitKey(0) # for image display
cv2.destroyAllWindows() # for image display