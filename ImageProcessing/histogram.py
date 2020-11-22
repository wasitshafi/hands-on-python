import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = 'airplane.png'

img = cv2.imread(file_name, 0)

cv2.imshow("Airplane", img)
cv2.waitKey(0)
