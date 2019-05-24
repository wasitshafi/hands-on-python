import cv2
                    # (0) for device index for using the webcam....else provide the video file name("vid.mp4")
cap = cv2.VideoCapture(0)                # for more info read : http://www.fourcc.org/codecs.php

fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc code is a 4 byte code used to specify the video codec 
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))# name of vide file, fourcc code, no of frames, size(maxx,maxy)
print ("Press 'q to exit() : ")

print ("isOpened = ", cap.isOpened(), end = "\n\n")
while(cap.isOpened()):
    ret, frame = cap.read() #'ret' is a boolean variable its value is True if the frame is available in the variable named 'frame' & where as 'frame' is used to store the frame captured
    
    if ret == True:
        print ("Width : ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print ("Height : ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)
        cv2.imshow("Frames", frame)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        print ("isOpened = ", cap.isOpened(), end = "\n\n")
    else:
        break
    

cap.release()
out.release()
cv2.destroyAllWindows()