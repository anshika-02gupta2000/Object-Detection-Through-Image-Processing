#Image processing using python


import cv2



img1=cv2.imread("images\Osteosarcoma_01.tif",0)
print(img1.shape)

cv2.imshow("Osteosarcoma",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#splitting channels
blue, green, red= cv2.split(img1)


