import cv2
import numpy as np

blackImage = np.zeros((512,512, 3), dtype = np.uint8)
whiteImage = np.zeros((512,512, 3), dtype = np.uint8)

# set to 255 method1 for white image
#for x in range(512):   # for more info read : https://stackoverflow.com/questions/10465747/how-to-create-a-white-image-in-python
#    for y in range(512):
#        whiteImage[x, y] = [255,255,255]

# method 2 for white image
whiteImage[:] = [255, 255, 255] # [:] = [255, 255, 255] this means fill all with the specified values]
 
print ("Black Image : ", blackImage)
print ("White Image : ", whiteImage)

cv2.imshow("Black image", blackImage)
cv2.imshow("White image", whiteImage)

cv2.waitKey(0)