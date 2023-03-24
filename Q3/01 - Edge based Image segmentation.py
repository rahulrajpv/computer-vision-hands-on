#Importing Libraries
import numpy as np 
import cv2 as cv2
# Read the input image
img = cv2.imread(r"D:\MTECH\PROJECT\CV\ASSIGNMENT\REPOSITORY\computer-vision-hands-on\Q5\dataset\Sample03.jpg") # for image read , r used for raw string that is to avoid escape sequence

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR to GRAY conversion

# Apply the Canny edge detector
edges = cv2.Canny(gray, 100, 200) # 100 and 200 are the thresholds for the hysteresis procedure and gray is the input image

# Display the resulting image
cv2.imshow("Edge based",edges) # for image display
cv2.waitKey(0) # for image display
cv2.destroyAllWindows() # for image display