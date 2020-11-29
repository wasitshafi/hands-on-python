import cv2
import numpy as np

file_name = "parrots.jpg"
img_parrots = cv2.imread(file_name)
img_parrots_grayscale = cv2.imread(file_name, 0)
cv2.imshow("Original image", img_parrots)
cv2.imshow("Original grayscale image", img_parrots_grayscale) # one of the simplest way to convert to grayscale is average of all 3 intensities g = (b+g+r)/3
img_parrots_blue, img_parrots_green, img_parrots_red = cv2.split(img_parrots)

cv2.imshow("Parrot Blue Channel", img_parrots_blue)
cv2.imshow("Parrot Green Channel", img_parrots_green)
cv2.imshow("Parrot Red Channel", img_parrots_red)

img_parrot_megred = cv2.merge([img_parrots_blue, img_parrots_green, img_parrots_red])
cv2.imshow("Parrot Imaged Merged 3 Channels", img_parrot_megred)

# Making our own gray scale image
h, w = len(img_parrots), len(img_parrots[0])
arr = [[0 for x in range(w)] for y in range(h)]

for i in range(h):
  for j in range(w):
    print(i, j)
    arr[i][j] = (img_parrots_blue[i][j] + img_parrots_green[i][j] + img_parrots_red[i][j]) // 3;

nparray = np.array(arr, dtype='uint8')
cv2.imshow("Grayscale image using average of 3 channels", nparray)
cv2.waitKey(0)
cv2.destroyAllWindows()