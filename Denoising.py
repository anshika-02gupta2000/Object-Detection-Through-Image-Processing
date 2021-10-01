##Denoising

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread("images\Osteosarcoma_01.tif",1)
img2= cv2.resize(img1, None,fx=0.4,fy=0.4, interpolation=cv2.INTER_CUBIC)

kernel=np.ones((3,3),np.float32)/9

filt_2D=cv2.filter2D(img2,-1,kernel)
blur = cv2.blur(img2,(3,3))
gaussian_blur = cv2.GaussianBlur(img2,(3,3),0)
median_blur = cv2.medianBlur(img2,3)
bilateral_blur = cv2.bilateralFilter(img2,9,75,75)


cv2.imshow("Original Image",img2)
cv2.imshow("2D custom filter",filt_2D)
cv2.imshow("blured",blur)
cv2.imshow("Median blured",median_blur)
cv2.imshow("Bilateral blured",bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()