import cv2
import numpy as np

def nothing(x):
    print(x)

print ("Press esc to exit :")
image = np.zeros( (512, 512, 3), dtype = np.uint8 )
cv2.namedWindow("Image")
 
cv2.createTrackbar('B', "Image", 0, 255, nothing) # on changing the track bar the function nothing will be automatically called
cv2.createTrackbar('G', "Image", 0, 255, nothing)
cv2.createTrackbar('R', "Image", 0, 255, nothing)

while(1):
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF 
    if key == 27: # 27 = esc key
        break
    
    b = cv2.getTrackbarPos('B', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    r = cv2.getTrackbarPos('R', 'Image')
    image[:] = [b, g, r]
    
cv2.destroyAllWindows()