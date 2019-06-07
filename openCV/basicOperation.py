import cv2

image = cv2.imread("messi.jpg", 1)
image2 = cv2.imread("cards.jpg", 1)

print ("Image shape : ", image.shape)
print ("Image size  : ", image.size)
print ("Image dtype : ", image.dtype)
print ("image : ", image)
b, g, r = cv2.split(image)
print ("b channel  : ", b)
print ("g channel  : ", g)
print ("r channel  : ", r)

image = cv2.merge((b, g, r)) # again merge the channels
ball = image[280:340, 330:390]
image[273:333, 100:160] = ball

cv2.imshow('Copy Ball', image)

image = cv2.resize(image, (512,512))
image2 = cv2.resize(image2, (512,512))
 
 #image2 is added to image
image3 = cv2.add(image, image2) # inorder to add 2 images the height and width of both the images must be same... is that have difrent size then resize the both the image to common size
cv2.imshow("add Images", image3)

image4 = cv2.addWeighted(image, .8, image2, .2, 0) #CMT .9 + .1 = 1 , last agr(0). is gamma.
image4 = cv2.addWeighted(image, .5, image2, .5, 0) #CMT .5 + .5 = 1 , last agr(0). is gamma.

cv2.imshow("addWeighted(.9,.1)", image4)
cv2.imshow("addWeighted(.5,.5)", image4)

cv2.waitKey(3000)
cv2.waitKey(0)
cv2.destroyAllWindows()