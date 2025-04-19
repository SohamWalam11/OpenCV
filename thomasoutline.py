import cv2 
import numpy as np

old_img = cv2.imread("thomas.jpg")
old_img_1 = cv2.resize(old_img,(400,400))

# CIRCLE 
# new_img = cv.circle(img=old_img,center=(220,180),radius=95,color=(0,255,0),thickness=4,lineType=16)

# ELLIPSE
# new_img = cv.ellipse(img=old_img, center=(220,180),axes=(50,100),angle=30, startAngle=0, endAngle=360, color=(0,255,0), thickness=4, lineType=4)
 
# TEXT ON IMAGE
text_img = cv2.putText(img=old_img_1,text="Thomas Shelby",org=(130,90),fontFace=1,fontScale=1,color=(0,255,255),thickness=1,lineType=4,bottomLeftOrigin=False)

# TEXT ON IMAGE
# new_img = cv.line(img = old_img,pt1=(120,100),pt2=(290,100),color=(0,255,0),thickness=2,lineType=4)

# RECTANGLE ON FACE OF IMAGE 
# new_img = cv.rectangle(img = text_img, pt1=(120,100),pt2=(290,250),color=(255,0,0),thickness=2,lineType=4)

# polygon on image (pentagon,hexa) 
new_im = cv2.polylines(img=old_img_1,pts=[np.array([[120,100],[310,100],[310,210],[260,250],[180,250],[120,210],[120,100]])],isClosed = False, color=(0,0,255),thickness=2,lineType=1)

cv2.imshow("Thomas",text_img)
cv2.imshow("Thomas",new_im)

cv2.waitKey(0)
cv2.destroyAllWindows()