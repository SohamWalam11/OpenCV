import cv2 as cv
import numpy as np

img_1 = cv.imread("glasses.jpg")
res_img = cv.resize(img_1,(300,300))

img_2 = cv.copyMakeBorder(res_img,5,5,5,5,cv.BORDER_CONSTANT,None,value = 1)
res_img_2 = cv.resize(img_2,(300,300))

img_3 = cv.copyMakeBorder(res_img,5,5,5,5,cv.BORDER_REFLECT,None,value = 1)
res_img_3 = cv.resize(img_3,(300,300))

h= np.hstack((res_img,res_img_2,res_img_3))
cv.imshow("Border",h)
cv.waitKey(0)
cv.destroyAllWindows()