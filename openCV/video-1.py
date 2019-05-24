import cv2

#this program will show the frame as it captures from the camera...
cap = cv2.VideoCapture(0)

# Video capture properties... for more info read : https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
print ("Frame width : ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print ("Frame height : ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print ("Frame TILT : ", cap.get(cv2.CAP_PROP_TILT))

print ("Press 'q' to exit() : ")
while(True):
    print ("Frame width : ", cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # CAPTURE_PROPERTY_FRAME_WIDTH
    print ("Frame height : ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT), end = "\n\n")

    ret, frame = cap.read() 
    cv2.imshow("Frames", frame)
        
#    k = cv2.waitKey(1) & 0xff   #(1) for the least time to read the value 
 #   if(k == ord("q")): 
  #     print ("break")
   #    break   
   
    # or use  shorthand form 
    if (cv2.waitKey(1) == ord('q') & 0xff ):
         break
cap.release()
cv2.destroyAllWindows()