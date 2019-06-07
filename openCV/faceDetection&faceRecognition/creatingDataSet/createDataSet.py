import cv2
import os

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

id = input("Enter user id : ")
sampleNum = 1
while(True):
    ret, image = cap.read()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grayImage, 1.3, 5) #(image, scale, min. neighbours )
    for (x, y, w, h) in faces:
        cv2.imwrite("dataSet/User_" + str(id) + "_" + str(sampleNum) + ".jpg", grayImage[y:y + h, x:x + w])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        sampleNum += 1
        cv2.waitKey(100)

    cv2.imshow("Face", image)
    cv2.waitKey(1)
    if(sampleNum > 30):
	    break

cv2.imshow("Face", image)
cv2.waitKey(2000)
cap.release()
cv2.destroyAllWindows()
