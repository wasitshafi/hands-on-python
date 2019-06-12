import cv2

image = cv2.imread("squareBoat.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(grayImage,1.3, 5)

print ("Total faces detected is : ", len(faces))
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("Face", image)
cv2.waitKey(0)
cv2.DestroyAllWindows()

# CTM Steps to detect the faces
#  : open image
#1 : create the object of "haarcascade_frontalface_default.xml" file  usually the name of that object is 'faceCascade'or'detect'
#2 : since the cascadeClassifier only works with grayscale image for detection so convert image to gray as pass as argument to detectMul.....(....)
#3 : assign detect.detectM.....(....)  to an object this will return all the points of x,y,w,h, for each faces detected. usually the name of that object taken as 'faces' its so because it contans the all corresponding values for the face region in the image
#4 : iterate that 'faces' object using 'for loop' to draw the rectangle around faces
#5 : show the image
