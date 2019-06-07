import cv2

print("This program will only open the camera to show the contents : ")
print ("Press 'q' to quit...")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)
    if(cv2.waitKey(1) == ord('q') & 0xff):
        break
cap.release()
cv2.destroyAllWindows()