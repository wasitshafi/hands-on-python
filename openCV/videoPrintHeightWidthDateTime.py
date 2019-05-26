import cv2
import datetime as dt
i = 0

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)  

while(cap.isOpened()):
    ret, frame = cap.read()
    
    dateTime = dt.datetime.now() 
    
    date = "Date : " + dateTime.strftime("%x")
    time = "Time :" + dateTime.strftime("%X")
    height = "Frame Height : " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
    width = "Frame width  : " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                      
    f = cv2.FONT_HERSHEY_DUPLEX 

    frame = cv2.putText(frame, date, (5, 15), f, .5, (9, 9, 188), 1, cv2.LINE_AA)     
    frame = cv2.putText(frame, time, (5, 35), f, .5, (9, 9, 188), 1, cv2.LINE_AA) 
    frame = cv2.putText(frame, height, (180, 15), f, .5, (9, 9, 188), 1, cv2.LINE_AA) 
    frame = cv2.putText(frame, width, (180, 35), f, .5, (9, 9, 188), 1, cv2.LINE_AA) 

    
    print ("Date = ", date)
    print ("Time = ", time)
    print ("Height = ", height)
    print ("Width = ", width) 
    print (i)
    i = i + 1
    
    cv2.imshow("Video", frame)

    if(cv2.waitKey(1) & 0xff == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()




