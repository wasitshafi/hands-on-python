import cv2
import datetime as dt

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    dateTime = dt.datetime.now() 
    
    dateTime = "Date : ", dateTime.strftime("%x"), "\nTime : ", dateTime.strftime("%X")
    heightWidth = "Frame Height : ", str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) , "\nFrame width : ", str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                      
    f = cv2.FONT_HERSHEY_DUPLEX 

    frame = cv2.putText(frame, dateTime, (50, 50), f, 5, (50, 50, 50), 10, cv2.LINE_AA) 
    frame = cv2.putText(frame, heightWidth, (50, 100), f, 5, (50, 50, 50), 10, cv2.LINE_AA) 
    
    print ("Date = ",dateTime )
    print ("Time = ", heightWidth)
    
    cv2.imshow("Video", frame)

    if(cv2.waitKey(1) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()




