
####edge detection



from skimage import io
from skimage.filters import roberts, sobel, scharr, prewitt
from skimage.transform import resize,rescale

img1=io.imread("images\Osteosarcoma_01.tif",as_gray=True)

img2= resize(img1, (200,200),anti_aliasing=True)

img3= rescale(img1, 1.0 / 4.0 , anti_aliasing=False)

edge_roberts= roberts(img3)
edge_sobel= sobel(img3)
edge_scharr= scharr(img3)
edge_prewitt= prewitt(img3)

from skimage.feature import canny
edge_canny = canny(img3)

io.imshow(edge_roberts)
io.imshow(edge_sobel)
io.imshow(edge_scharr)
io.imshow(edge_prewitt)


