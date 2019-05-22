#import cv2

i = cv2.imread("card.jpg", 0)
cv2.imshow("New name", i)
cv2.waitKey(0)
cv2.destroyAllWindows()