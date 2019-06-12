import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read() #cap.read() returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of the video by checking this return value.
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convertcolor(....)
    faces = faceCascade.detectMultiScale(grayFrame, 1.5, 5)
    print ("Total faces detected : ", len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w,y + h), (50, 255, 50), 2)

    msg = "Total Faces : " + str(len(faces)) 
    cv2.putText(frame, msg, (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .5, (50, 255, 50), 2)
    
    cv2.imshow("Face", frame)
    
    if(cv2.waitKey(1) == ord('q') & 0xff):
            break

cap.release()
cv2.destroyAllWindows()


# CTM Steps to detect the faces
#  : open image
#1 : create the object of "haarcascade_frontalface_default.xml" file  usually the name of that object is 'faceCascade' or 'detect'
#2 : since the cascadeClassifier only works with grayscale image for detection so convert image to gray as pass as argument to detectMul.....(....)
#3 : assign detect.detectM.....(....)  to an object this will return all the points of x,y,w,h, for each faces detected. usually the name of that object taken as 'faces' its so because it contans the all corresponding values for the face region in the image
#4 : iterate that 'faces' object using 'for loop' to draw the rectangle around faces
#5 : show the image