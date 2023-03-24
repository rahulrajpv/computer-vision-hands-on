import pywt
import numpy as np
import cv2

# Load the image
img = cv2.imread(r"C:\Users\rahul\OneDrive\Pictures\sample03.jpg", 0)

# Resize the image to a new width and height
width = 500 # new width in pixels
height = 300 # new height in pixels
resized_img = cv2.resize(img, (width, height)) # resize the image


# Perform the DWT using the 'haar' wavelet
coeffs = pywt.dwt2(img, 'haar') # returns a tuple of 4 arrays (cA, (cH, cV, cD))

# Separate the coefficients into approximation and detail coefficients
cA, (cH, cV, cD) = coeffs # cA is the approximation coefficients, cH, cV, cD are the detail coefficients

# Display the original image and the DWT coefficients
cv2.imshow('Original Image', img) # original image
cv2.imshow('Approximation Coefficients', np.uint8(cA)) # approximation coefficients
cv2.imshow('Horizontal Detail Coefficients', np.uint8(cH)) # detail coefficients
cv2.imshow('Vertical Detail Coefficients', np.uint8(cV)) # detail coefficients
cv2.imshow('Diagonal Detail Coefficients', np.uint8(cD)) # detail coefficients 
cv2.waitKey(0) # wait for a key press
cv2.destroyAllWindows() # close all windows

