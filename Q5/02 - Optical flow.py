import cv2
import numpy as np

# Read input video
cap = cv2.VideoCapture(r"D:\MTECH\PROJECT\CV\ASSIGNMENT\REPOSITORY\computer-vision-hands-on\Q5\dataset\Sample01.mp4")

# Create object for optical flow
prev_frame = None
hsv = None

# Iterate through video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate optical flow using Lucas-Kanade method
    if prev_frame is not None:
        flow = cv2.calcOpticalFlowFarneback(prev_frame, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        
        # Convert flow vectors to polar coordinates
        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        
        # Normalize magnitude values
        mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        
        # Convert angle values to hue channel
        hsv[...,0] = ang * 180 / np.pi / 2
        
        # Set value channel to normalized magnitude values
        hsv[...,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        
        # Convert HSV image back to BGR for display
        optical_flow = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        
        # Display optical flow image
        cv2.imshow('Optical Flow', optical_flow)
        
    # Update previous frame
    prev_frame = gray.copy()
    
    # Create object for HSV image
    if hsv is None:
        hsv = np.zeros_like(frame)
        hsv[...,1] = 255
        
    # Wait for key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
