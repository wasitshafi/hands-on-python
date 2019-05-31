import cv2
import numpy as np
import PIL

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(image):
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grayImage, 1.3, 5)

    if faces is ():
        return None
    for(x, y, w, h) in faces:
        cropped_face = image[y:y + h, x:x + w]
    return cropped_face

cap = cv2.VideoCapture(0) # 0 is device index
count = 0
        
while(True):
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        path='dataset/'+str(count)+'.jpg'
        cv2.imwrite(path, face)
        cv2.putText(face, str(count),(50, 50),cv2.FONT_HERSHEY_COMPLEX,1,(0, 255, 0),2)
        cv2.imshow('Face Detection', face)
    else:
        print('Face not found')
    
    if cv2.waitKey(1) == ord('q') & 0xff or count == 20:
        break
cap.release()
cv2.destroyAllWindows()