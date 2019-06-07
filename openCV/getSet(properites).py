import cv2

cap = cv2.VideoCapture(0)  # don't forget 'V' in upper case

#the camer will try to implement the width & height you mention & if not possible as it also has to maintain the resolution 
#of the camera in that case it will try to implement the most simillar frame width and height you mentioned

# get() is used to reterive the value
# set() is used to modify the value

print ("DEFAULT : ")
cap = cv2.VideoCapture(0)
print ("Frame height = ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print ("Frame WIDTH = ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)  
print ("\n\nAfter trying frame width = 1000 & frame height = 900")

print ("Frame height = ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print ("Frame WIDTH = ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if (ret == True):
        cv2.imshow("Video", frame)
        if (cv2.waitKey(1) & 0xff == ord('q')):
          break
    else:
        break
    
cap.release()    
cv2.destroyAllWindows()