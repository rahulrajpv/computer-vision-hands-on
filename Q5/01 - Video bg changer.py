#importing libraries
import cv2 as cv2#for image processing
import cvzone #for image processing
from cvzone.SelfiSegmentationModule import SelfiSegmentation #cvzone.SelfiSegmentationModule is a module that is used to remove the background from an image

# Load the video and the background image
# Read input video
vid = cv2.VideoCapture(r"D:\MTECH\PROJECT\CV\ASSIGNMENT\REPOSITORY\computer-vision-hands-on\Q5\dataset\Sample01.mp4")
bg_img = cv2.imread(r"D:\MTECH\PROJECT\CV\ASSIGNMENT\REPOSITORY\computer-vision-hands-on\Q5\dataset\Sample03.jpg") #sample01.jpg is the background image

# Get the size of the video frame
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)) # 1280 pixels wide (width)
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 720 pixels high (height)

# Resize the background image to match the video frame size
bg_img = cv2.resize(bg_img, (width, height)) # (1280, 720)

# Initialize the SelfiSegmentation object
seg = SelfiSegmentation() # SelfiSegmentation() is a class that is used to remove the background from an image

# Loop through the frames of the video
while True:
    # Read a frame from the video
    _, frame = vid.read()

    # Check if the frame was successfully read
    if not _:
        break # break is used to exit the loop

    # Remove the background from the frame using the background image
    frame_rmbg = seg.removeBG(frame, bg_img, threshold=0.8) # removeBG() is a method that is used to remove the background from an image

    # Display the resulting image
    cv2.imshow("Video", frame_rmbg) # frame_rmbg is the frame without the background

    # Check if the user pressed the 'x' key to exit
    if cv2.waitKey(1) == ord('x'): # ord() function returns the unicode code point for the specified character and waitKey() is a keyboard binding function
        break # break is used to exit the loop if the user pressed the 'x' key to exit the loop and exit the program

# Release the video capture and destroy the windows
vid.release() # release() is used to release the video capture
cv2.destroyAllWindows() # destroyAllWindows() is used to destroy all the windows created by the program
