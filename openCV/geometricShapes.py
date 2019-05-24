import cv2

image = cv2.imread("plant.jpg", 1)

# CTM: color must be in BGR format unlike regular RGB format

image = cv2.line(image, (0, 0), (350, 50), (0, 0, 255), 6)        #(image, (startPoint), (endPont), color, thickness)    
image = cv2.arrowedLine(image, (0, 0), (50, 350 ), (0, 255, 0), 6) #(image, (startPoint), (endPont), color, thickness)    

image = cv2.rectangle(image, (400, 100), (600, 250), (255, 255, 0), 10) #(image, (topLeftpoint), (bottomRightPoint),(color),thickness)  
image = cv2.rectangle(image, (700, 100), (900, 250), (0, 255, 255), -1) #here -1 specifies to fill the rectangle with color

image = cv2.circle(image, (350, 600), 100, (20, 20, 20), 5)     #(image, center, radius, (color) , thickness)
image = cv2.circle(image, (700, 600), 100, (100, 100, 100), -1) #(image, center, radius, (color) , -1) # -1  to fill the circle with color mentioned
                  
f = cv2.FONT_HERSHEY_DUPLEX                
image = cv2.putText(image, 'Hello World...', (150, 400), f, 5, (50, 200, 100), 10, cv2.LINE_AA)  #(image, text, startPoint,fontface, fontsize, color, thickness, linetype)                

cv2.imshow("title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()