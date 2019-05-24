import cv2

imageGrayScale = cv2.imread("fruits.jpg", 0)    # read in color mode
cv2.imwrite("fruits_copy.jpg", imageGrayScale)  # creating the copy of the image
cv2.waitKey(0)
