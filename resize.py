##resizing

import cv2

img1=cv2.imread("images\Osteosarcoma_01.tif",1)
resized= cv2.resize(img1, None,fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)
print(resized.shape)

cv2.imshow("Original Image",img1)
cv2.imshow("resized Image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()