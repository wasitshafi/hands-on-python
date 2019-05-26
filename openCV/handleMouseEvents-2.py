import cv2

def MyClickEvent(event, x, y, flat, param):
    if (event == cv2.EVENT_LBUTTONDOWN): 
        points.append((x,y))
         
        if(len(points) >= 2):
            cv2.line(image, points[-1], points[-2], (255, 0, 0), 5)
        else:
            cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
        
        cv2.imshow("Image", image)
        
image = cv2.imread("messi.jpg", 1)
cv2.imshow("Image", image)
points = [] #creating an empty list

cv2.setMouseCallback("Image", MyClickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()