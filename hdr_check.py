import cv2
import matplotlib.pyplot as plt

# Open HDR
hdr = cv2.imread('E:\\spectrum-tuner\\final_room1.hdr', cv2.IMREAD_COLOR)


# Rescale 
scale = 1
hdr = cv2.resize(hdr, None, fx=scale, fy=scale, interpolation = cv2.INTER_AREA)

print(type(hdr))
print(hdr.shape)

color = ('b', 'g', 'r')

for i,col in enumerate(color):
    histr = cv2.calcHist(hdr, [i], None, [1000], [0,256])
    plt.plot(histr, color = col)
    plt.xlim([0,256])

#plt.plot(hist)
plt.show()