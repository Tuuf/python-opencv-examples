import cv2
import numpy

face=cv2.CascadeClassifier("haarcascade_fullbody.xml")
photo=cv2.imread("boy.png")
gray=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)

faces=face.detectMultiScale(gray,1.1,4)
print(faces)
for (x,y,w,h) in faces:
    cv2.rectangle(photo,(x,y),(x+w,y+h),(345,5,0),5)

cv2.imshow("photo",photo)
cv2.waitKey(0)
cv2.destroyAllWindows()