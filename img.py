import cv2 as cv
import numpy as np

old_img = cv.imread("thomas.jpg")


# CIRCLE 
# new_img = cv.circle(img=old_img,center=(220,180),radius=95,color=(0,255,0),thickness=4,lineType=16)

# ELLIPSE
# new_img = cv.ellipse(img=old_img, center=(220,180),axes=(50,100),angle=30, startAngle=0, endAngle=360, color=(0,255,0), thickness=4, lineType=4)
 
# TEXT ON IMAGE
# text_img = cv.putText(img=old_img,text="Thomas",org=(130,90),fontFace=2,fontScale=1,color=(0,0,255),thickness=1,lineType=16,bottomLeftOrigin=False)

# TEXT ON IMAGE
# new_img = cv.line(img = old_img,pt1=(120,100),pt2=(290,100),color=(0,255,0),thickness=2,lineType=4)

# RECTANGLE ON FACE OF IMAGE 
# new_img = cv.rectangle(img = text_img, pt1=(120,100),pt2=(290,250),color=(255,0,0),thickness=2,lineType=4)

# polygon on image (pentagon,hexa) 
new_im = cv.polylines(img=old_img,pts=[np.array([[120,100],[310,100],[310,210],[260,250],[180,250],[120,210],[120,100]])],isClosed = False, color=(0,0,255),thickness=2,lineType=1)
cv.imshow("Thomas",new_im)

cv.waitKey(0)
cv.destroyAllWindows()