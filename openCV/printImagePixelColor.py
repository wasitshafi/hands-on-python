import cv2

def MyMouseEvent(event, x, y, flat, param):
    global image
    if (event == cv2.EVENT_MOUSEMOVE):
        blue = image[y, x, 0] # CTM [y axis, x axis, channel] to get the color info. at the poition x,y ..... 0 is for blue channel, 1 for green channel and  2 for red channel
        green = image[y, x, 1]
        red = image[y, x, 2]
        msgBGR = "BGR(" + str(blue) + ", " +  str(green) + ", " + str(red) + ")"
        msgXY = "X = " + str(x) + "   Y = " + str(y)
         
        print ("Right Button Down Event.")    
        print (msgBGR, end = "\n\n")
        font = cv2.FONT_HERSHEY_SIMPLEX
        image = cv2.imread("cards.jpg", 1)
        cv2.putText(image, msgBGR, (5, 15), font, .5, (34, 34, 178), 2)  
        cv2.putText(image, msgXY, (5, 35), font, .5, (34, 34, 178), 2)
        cv2.imshow("Image", image)

image = cv2.imread("cards.jpg", 1)
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", MyMouseEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()