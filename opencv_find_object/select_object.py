import cv2
import numpy as np



img_rgb=cv2.imread('anaresim')
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

nesne=cv2.imread('templar',0)

w,h=nesne.shape[::-1]

res=cv2.matchTemplate(img_gray,nesne,cv2.TM_CCOEFF_NORMED) 
#Template Matching is a method for searching and finding the location of a template image in a larger image. OpenCV comes with a function cv2.matchTemplate() for this purpose
threshold=0.8

loc=np.where(res>threshold) 
#numpy.where(condition[, x, y])Return elements chosen from x or y depending on condition.


for n in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,n,(n[0]+w,n[1]+h),(14,240,255),2)

cv2.imshow('bulunan nesneler',img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
