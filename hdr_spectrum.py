import cv2
import numpy as np
import matplotlib.pyplot as plt

def RGBtoWavelength(r, g, b):
    # Convert RGB values to X, Y, and Z values
    X = 0.412453 * r + 0.357580 * g + 0.180423 * b
    Y = 0.212671 * r + 0.715160 * g + 0.072169 * b
    Z = 0.019334 * r + 0.119193 * g + 0.950227 * b

    # Convert XYZ values to wavelength
    n = (X + Y + Z)
    x = X / n
    y = Y / n
    lambda_ = 442.0 * (1.0 - x) / (y + 0.065)
    
    return lambda_

# Load the HDR image using cv2
img = cv2.imread('E:\\spectrum-tuner\\final_room1.hdr', cv2.IMREAD_UNCHANGED)

# Rescale 
scale = .1
img = cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_AREA)

# Convert the HDR image to a 8-bit representation
img_8bit = np.uint8(img * 256)

# Split the image into its RGB channels
b, g, r = cv2.split(img_8bit)

# Apply the RGBtoWavelength function to the B, G, and R values
wavelengths = np.zeros_like(b)
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        wavelengths[i, j] = RGBtoWavelength(r[i, j], g[i, j], b[i, j])

# Compute the histograms for the wavelengths
#hist_wavelengths = cv2.calcHist([wavelengths], [0], None, [256], [0, 256])

# Plot the histograms using matplotlib
plt.plot(wavelengths, color='purple')
plt.show()