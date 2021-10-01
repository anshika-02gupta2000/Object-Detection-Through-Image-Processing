### Histogram Equalization####
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread("images\Osteosarcoma_01.tif",0)
img2= cv2.resize(img1, None,fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)
eq_image=cv2.equalizeHist(img2)

plt.hist(img2.flat, bins=100, range=(100,200))
plt.hist(eq_image.flat)

cv2.imshow("Equalized Image",eq_image)
cv2.waitKey(0)
cv2.destroyAllwindow()
