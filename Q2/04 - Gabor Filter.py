import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('/content/sample01.jpg', cv2.IMREAD_GRAYSCALE)


# Define the Gabor filter parameters
ksize = 31  # kernel size
sigma = 5  # standard deviation of Gaussian envelope
gamma = 0.5  # spatial aspect ratio
phi_arr = [0, 0, 90, 150]  # orientation of the normal to the parallel stripes of a Gabor function
lambda_arr = [20, 80, 30, 10]  # wavelength of the sinusoidal factor
# Create the figure with a larger size
fig, axs = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))
# Create the Gabor filter kernel for each parameter combination and apply the filter to the image
for i in range(len(phi_arr)):
    theta = phi_arr[i] * np.pi / 180
    lambd = lambda_arr[i]
    kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, 0, ktype=cv2.CV_32F)
    filtered = cv2.filter2D(img, cv2.CV_8UC3, kernel)

    # Display the original and filtered images
    plt.subplot(2, 4, i+1), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 4, i+5), plt.imshow(filtered, cmap='gray'), plt.title(f'Gabor Filtered\nPhi: {phi_arr[i]}, Lambda: {lambda_arr[i]}')
    plt.xticks([]), plt.yticks([])

plt.show()
