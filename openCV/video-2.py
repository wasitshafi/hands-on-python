import cv2

#this program will show the frame as it captures from the camera...
cap = cv2.VideoCapture(0)
print ("Press 'q to exit() : ")
while(True):
    ret, frame = cap.read() #'ret' is a boolean variable its value is True if the frame is available in the variable named 'frame' & where as 'frame' is used to store the frame captured
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Frames", gray)
    
    #k = cv2.waitKey(1) & 0xff    #1 for the least time to read the value
    #if(k == ord("q")): 
    #  print ("break")
    #   break   
   
    # or use the shorthand form
   if(cv2.waitKey(1) & 0xff == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()