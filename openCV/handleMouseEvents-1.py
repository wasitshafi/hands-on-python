import cv2

def MyClickEvent(event, x, y, flat, param):
    if (event == cv2.EVENT_LBUTTONDOWN):
        msg = "P(" + str(x) + ", " +  str(y) + ")"
        print ("Left Button down Event")
        print (msg, end = "\n\n")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, msg, (x , y), font, .5, (255,0, 5), 2)
        cv2.imshow("Image", image)
        
    if (event == cv2.EVENT_RBUTTONDOWN): 
        blue = image[y, x, 0] # CTM [y axis, x axis, channel] to get the color info. at the poition x,y ..... 0 is for blue channel, 1 for green channel and  2 for red channel
        green = image[y, x, 1]
        red = image[y, x, 2]
        msg = "BGR(" + str(blue) + ", " +  str(green) + "," + str(red) + ")"
        print ("Right Button down Event.")    
        print (msg, end = "\n\n")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, msg, (x , y), font, .5, (255,0, 5), 2)
        cv2.imshow("Image", image)

print("List of all Mouse Events : ")
x = [i for i in dir(cv2) if "EVENT" in i]
print (x)
            
image = cv2.imread("cards.jpg", 1)
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", MyClickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()