import cv2

file_name = 'airplane.png'
img = cv2.imread(file_name)
#img = cv2.imread(file_name, 0) # or reading image directly as grayscale

cv2.imshow('Color Image', img)

imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Gray Scale Image
cv2.imshow('Gray Scale Image', imgG)
cv2.waitKey(0) # when we press 0 window will terminate
