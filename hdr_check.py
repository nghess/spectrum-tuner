import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the HDR image using cv2
img = cv2.imread('E:\\spectrum-tuner\\final_room1.hdr', cv2.IMREAD_UNCHANGED)

#print(img[:,:,0])

# Rescale 
scale = .1
img = cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_AREA)

# Convert the HDR image to a 8-bit representation
img_8bit = np.uint8(img * 256)

# Split the image into its RGB channels
b, g, r = cv2.split(img_8bit)

# Compute the histograms for each channel
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Plot the histograms using matplotlib
plt.plot(hist_b, color='blue')
plt.plot(hist_g, color='green')
plt.plot(hist_r, color='red')
plt.show()

