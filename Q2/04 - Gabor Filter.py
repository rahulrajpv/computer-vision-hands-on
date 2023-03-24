#import the necessary packages
import numpy as np
import cv2

# Load the image
img = cv2.imread(r"C:\Users\rahul\OneDrive\Pictures\sample03.jpg",0)

# Define the Gabor filter parameters
ksize = 31  # kernel size
sigma = 5  # standard deviation of Gaussian envelope
theta = np.pi / 4  # orientation of the normal to the parallel stripes of a Gabor function
lambd = 10  # wavelength of the sinusoidal factor
gamma = 0.5  # spatial aspect ratio

# Create the Gabor filter kernel
kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, 0, ktype=cv2.CV_32F) # ktype = cv2.CV_32F for float32   

# Apply the Gabor filter to the image
filtered = cv2.filter2D(img, cv2.CV_8UC3, kernel) # cv2.CV_8UC3 for float32 to uint8 conversion 

# Display the original and filtered images
cv2.imshow("Original", img)
cv2.imshow("Gabor Filtered", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
