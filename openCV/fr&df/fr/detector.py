import cv2
import numpy as numpy
import os
from PIL import Image
faceDetect = cv2.CascadeClassifier("C:/Users/jhon pc/Desktop/python3/openCV/fr&df/fr/harcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("C:/Users/jhon pc/Desktop/python3/openCV/fr&df/fr/trainningData.yml")


font = cv2.FONT_HERSHEY_DUPLEX   
id = 0

while(True):
    ret , image = cap.read()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grayImage, 1.3, 5)
	    
    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y +h), (0, 0, 255), 2)
        id, conf = rec.predict(grayImge[y:y+h, x:x+h])
        cv2.cv.PutText(cv2.cv.fromarray(image), str(id), (x, y + h), font, 255)
    cv2.imshow("Face", image)
    if(cv2.waitKey(1) == ord('q') & 0xff):
        break
cap.release()
cv2.destroyAllWindows()

