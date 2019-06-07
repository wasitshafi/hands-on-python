import cv2

image = cv2.imread("messi.jpg", 1)

print ("image : ", image)
b, g, r = cv2.split(image)
print ("b channel  : ", b)
print ("g channel  : ", g)
print ("r channel  : ", r)

image= cv2.merge((b, g, r))
cv2.imshow('BGR Channel Image', image)
cv2.waitKey(2000)

b, g, r = cv2.split(image)
image2= cv2.merge((b, b,g))
cv2.imshow('BBG Channel Image', image2)
cv2.waitKey(2000)

b, g, r = cv2.split(image)
cv2.imshow('B Channel Image', b)
cv2.waitKey(2000)
cv2.imshow('G Channel Image', g)
cv2.waitKey(2000)
cv2.imshow('R Channel Image', r)
cv2.waitKey(2000)

cv2.waitKey(0)
cv2.destroyAllWindows()