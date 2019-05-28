import cv2
import numpy as np

print ("Press 'q' to quit...")
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret,image = cap.read()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grayImage, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 150), 2)
    cv2.imshow("Faces", image)
    
    if(cv2.waitKey(1) ==  ord('q') & 0xff):
        break
cap.release()
cv2.destroyAllWindows()