import cv2
import numpy as np

# Read input video
cap = cv2.VideoCapture(r"D:\MTECH\PROJECT\CV\ASSIGNMENT\REPOSITORY\computer-vision-hands-on\Q5\dataset\Sample01.mp4") #sample01.mp4 is the input video

# Create object for optical flow
prev_frame = None #prev_frame is the previous frame
hsv = None #hsv is the hue saturation value

# Iterate through video frames
while cap.isOpened(): #isOpened() is used to check if the video is opened or not
    ret, frame = cap.read() #read() is used to read the video frame by frame
    if not ret: #if the video is not opened then 
        break #break is used to exit the loop
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cvtColor() is used to convert the frame from BGR to grayscale and BGR2GRAY is the flag used to convert the frame from BGR to grayscale
    
    # Calculate optical flow using Lucas-Kanade method
    if prev_frame is not None: #if the previous frame is not None then 
        flow = cv2.calcOpticalFlowFarneback(prev_frame, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0) #calcOpticalFlowFarneback() is used to calculate the optical flow using the Lucas-Kanade method and None is the input image, 0.5 is the pyr_scale, 3 is the levels, 15 is the winsize, 3 is the iterations, 5 is the poly_n, 1.2 is the poly_sigma, 0 is the flags
        
        # Convert flow vectors to polar coordinates
        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1]) #cartToPolar() is used to convert the flow vectors to polar coordinates and flow[...,0] is the x component of the flow vector and flow[...,1] is the y component of the flow vector
        
        # Normalize magnitude values
        mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX) #normalize() is used to normalize the magnitude values and cv2.NORM_MINMAX is the flag used to normalize the magnitude values
        
        # Convert angle values to hue channel
        hsv[...,0] = ang * 180 / np.pi / 2 #np.pi is the value of pi and /2 is used to convert the angle values to hue channel
        
        # Set value channel to normalized magnitude values
        hsv[...,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX) #cv2.NORM_MINMAX is the flag used to normalize the magnitude values
        
        # Convert HSV image back to BGR for display
        optical_flow = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) #cv2.COLOR_HSV2BGR is the flag used to convert the HSV image back to BGR for display
        
        # Display optical flow image
        cv2.imshow('Optical Flow', optical_flow) #optical_flow is the optical flow image
        
    # Update previous frame
    prev_frame = gray.copy() #copy() is used to copy the grayscale frame to the previous frame
    
    # Create object for HSV image
    if hsv is None: #if the hsv is None then
        hsv = np.zeros_like(frame) #zeros_like() is used to create an object for the HSV image
        hsv[...,1] = 255 #hsv[...,1] is the saturation channel of the HSV image
        
    # Wait for key press
    if cv2.waitKey(1) == ord('q'): #waitKey() is used to wait for a key press and ord('q') is used to exit the loop
        break #break is used to exit the loop 

# Release video capture and close windows
cap.release() #release() is used to release the video capture
cv2.destroyAllWindows() #destroyAllWindows() is used to close all the windows
