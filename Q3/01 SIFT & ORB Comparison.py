#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import os

# Load the image
path = os.path.join(r"C:\Users\reema\Downloads\img.jpg")
img = cv2.imread(path)

# Create SIFT and ORB object
sift = cv2.SIFT_create()
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors using SIFT
kp_sift, des_sift = sift.detectAndCompute(img, None)

# Detect keypoints and compute descriptors using ORB
kp_orb, des_orb = orb.detectAndCompute(img, None)

# Define the list of transformations to apply to the image
transforms = ['scale', 'rotate', 'affine', 'perspective']

# Loop over the transformations
keypoints = {'SIFT': {}, 'ORB': {}}
for transform in transforms:

    # Apply the transformation to the image
    if transform == 'scale':     
        img_transformed = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)   
    elif transform == 'rotate':         
        rows, cols = img.shape[:2]     
        M = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1)     
        img_transformed = cv2.warpAffine(img, M, (cols, rows))     
    elif transform == 'affine':      
        rows, cols = img.shape[:2]        
        pts1 = np.float32([[50, 50], [200, 50], [50, 200]])   
        pts2 = np.float32([[10, 100], [200, 50], [100, 250]])    
        M = cv2.getAffineTransform(pts1, pts2)
        img_transformed = cv2.warpAffine(img, M, (cols, rows))
    elif transform == 'perspective':
        rows, cols = img.shape[:2]
        pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        img_transformed = cv2.warpPerspective(img, M, (300, 300))

    # Detect keypoints and compute descriptors using SIFT
    kp_sift_transformed, des_sift_transformed = sift.detectAndCompute(img_transformed, None)

    # Detect keypoints and compute descriptors using ORB
    kp_orb_transformed, des_orb_transformed = orb.detectAndCompute(img_transformed, None)

    # Add the number of keypoints detected by SIFT and ORB to the dictionary
    keypoints['SIFT'][transform] = len(kp_sift_transformed)
    keypoints['ORB'][transform] = len(kp_orb_transformed)

    # Print the number of keypoints detected by SIFT and ORB in the original and transformed images
    print(f'{transform}: SIFT: {len(kp_sift)}, {len(kp_sift_transformed)}; ORB: {len(kp_orb)}, {len(kp_orb_transformed)}')

# Determine which keypoint extractor is better for each transformation
print('SIFT vs ORB:')
for transform in transforms:
    if keypoints['SIFT'][transform] > keypoints['ORB'][transform]:
        print(f'{transform}: SIFT is better')
    elif keypoints['SIFT'][transform] < keypoints['ORB'][transform]:
        print(f'{transform}: ORB is better')


# In[ ]:



