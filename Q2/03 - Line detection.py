import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread(r"C:\Users\rahul\OneDrive\Pictures\12_005__86834_1200x1200.jpg", 0)

# Resize the image
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Apply edge detection method on the image
edges = cv2.Canny(img, 50, 150, apertureSize=3)

# This returns an array of r and theta values
lines = cv2.HoughLines(edges, 1, np.pi/180, 350)

if lines is not None:
    for r_theta in lines:
           arr = np.array(r_theta[0], dtype=np.float64)
           r, theta = arr
           # Stores the value of cos(theta) in a
           a = np.cos(theta)
           # Stores the value of sin(theta) in b
           b = np.sin(theta)
           # x0 stores the value rcos(theta)
           x0 = a*r
           # y0 stores the value rsin(theta)
           y0 = b*r
           # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
           x1 = int(x0 + 1000*(-b))
           # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
           y1 = int(y0 + 1000*(a))
           # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
           x2 = int(x0 - 1000*(-b))
           # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
           y2 = int(y0 - 1000*(a))
           # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
           # (255, 255, 255) denotes the colour of the line to be drawn. In this case, it is white.
           cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 1)
else:
    print("No lines detected in the image")

# Display the image with detected lines
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
