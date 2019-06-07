import cv2

# -1 for load image including alpha channel, 0 for load image as gray scale, 1 for load color image
image = cv2.imread("cards.jpg", 1)

print ("Image = ", image)

for i in image:
    print (i)
    
cv2.imshow("title", image)
cv2.waitKey(5000)           # window will open for 6 sec. use waitKey(0) so to keep window opened until user close the window
cv2.destroyAllWindows()