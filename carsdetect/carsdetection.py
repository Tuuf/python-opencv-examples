import cv2
video=cv2.VideoCapture("CarsDrivingUnderBridge.mp4")
araba_bulucu=cv2.CascadeClassifier("cars.xml")
while True:
    ret,kare=video.read()

    griton=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    arabalar=araba_bulucu.detectMultiScale(griton,1.1,3)

    for (x,y,w,h) in arabalar:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.imshow("video",kare)


        if cv2.waitKey(5) & 0xFF == ord('q'):
            break


video.relase()
cv2.destroyAllWindows()