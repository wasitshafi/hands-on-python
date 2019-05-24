import cv2

image = cv2.imread("cards.jpg", 0)

print ("Image = ", image)

for i in image:
    print (i)
print ("Press 's' key to save the image or press 'esc' to close the window.")
    
cv2.imshow("title", image)
k = cv2.waitKey(0) & 0xff # its better to use the mask 0xff with wait key...so to make it compatible with both 32 & 64 bit systems

if k == 27 :
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("cards_copy.jpg", image)
    cv2.destroyAllWindows()
else:
    print ("Invalid choice...!")
