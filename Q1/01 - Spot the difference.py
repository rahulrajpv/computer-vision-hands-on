# Importing Libraries 
import cv2 #importing the opencv library
import imutils #importing the imutils library 

# Reading the sample images that we have taken for comparison and resizing them
image01 = cv2.imread(r"C:\Users\rahul\OneDrive\Pictures\Compare_01.jpg")
image01_resized = imutils.resize(image01, width=500) #resizing the image
image02 = cv2.imread(r"C:\Users\rahul\OneDrive\Pictures\Compare_02.jpg")
image02_resized = imutils.resize(image02, width=500) #resizing the image

# Create a copy of the original image so that we can store the difference of 2 images in the same one
diff = image01_resized.copy() #copying the image01_resized to diff variable 

# Finding the absolute difference between the 2 images and storing it in diff variable
cv2.absdiff(image01_resized, image02_resized, diff) # we are finding the absolute difference between the image01_resized and image02_resized and storing it in the diff variable

# converting the difference into grayscale images so that we can find the contours in the image
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # we are converting the diff image into grayscale image so that we can find the contours in the image
  
# increasing the size of differences after that we can capture them all in the contours
for i in range(0, 3): # we are increasing the size of the image 3 times so that we can capture all the differences in the image
    dilated = cv2.dilate(gray.copy(), None, iterations= i+ 1) #dilate function is used to increase the size of the image

# threshold the gray image to binary it. Anything pixel that has value higher than 3 we are converting to white (remember 0 is black and 255 is exact white) the image is called binarised as any value lower than 3 will be 0 and all of the values equal to and higher than 3 will be 255
(T, thresh) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY) # we are converting the image into binary image
  
# now we have to find contours in the binarized image
contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # we are finding the contours in the image
contours = imutils.grab_contours(contours) # we are grabbing the contours from the image

for c in contours:
    # Nicely fitting a bounding box to the contour
    (x, y, w, h) = cv2.boundingRect(c) # we are finding the bounding box for the contours
    cv2.rectangle(image02_resized, (x, y), (x + w, y + h), (0, 255, 0), 2) # we are drawing the rectangle around the contours in the image  and we are using the image02_resized image to draw the rectangle
    #0, 255, 0 is the color of the rectangle and 2 is the thickness of the rectangle. x and y are the starting point of the rectangle and x+w and y+h are the ending point of the rectangle

# Show the difference image
cv2.imshow("Difference", image02_resized) # we are showing the image02_resized image
cv2.waitKey(0) # we are waiting for the user to press any key
cv2.destroyAllWindows() # we are destroying all the windows
