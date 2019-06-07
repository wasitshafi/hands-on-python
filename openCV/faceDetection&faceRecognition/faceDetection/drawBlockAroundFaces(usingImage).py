import cv2
import numpy as np
import PIL

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread("squareBoat.jpg")
image2 = cv2.imread("team.jpg")

image = cv2.resize(image, (1366, 750))
image2 = cv2.resize(image2, (1366, 750))

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayImage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

faces = faceDetect.detectMultiScale(grayImage, 1.3, 5)
print ("Total face detected from  is : ", len(faces))
count = 1
font = cv2.FONT_HERSHEY_SIMPLEX
for(x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 150), 2)
	cv2.putText(image, str(count), (x+5, y-5), font, 1, (50, 50, 255), 2)
	count += 1
faces = faceDetect.detectMultiScale(grayImage2, 1.3, 5)
print ("Total face detected from  is : ", len(faces))
count = 1
for(x, y, w, h) in faces:
	cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 255, 150), 2)
	cv2.putText(image2, str(count), (x+5, y-5), font, 1, (50, 50, 255), 2)
	count += 1
cv2.imshow("SquareBoad", image)
cv2.imshow("Team", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()   