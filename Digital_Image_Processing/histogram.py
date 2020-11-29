import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading Image
file_name = 'airplane.png'
img = cv2.imread(file_name, 0)

print(img)
#cv2.imshow("US Airplane", img)

# Printing Image Dimensions
print("Image Dimensions   :", len(img), "X", len(img[0]))
print("Total No Of Pixels :", len(img) * len(img[0]))


# Array to count frequency
frequency = [0] * 256
for i in range(len(img)):
  for j in range(len(img[i])):
    frequency[img[i][j]] += 1;

# Plot Graph
plt.plot(list(range(256)), frequency)
plt.xlabel("Intensity / Gray Scale Value")
plt.ylabel("Frequency")
plt.show() # The spike towards right side is due to high no of white pixel(snow  in image)

cv2.waitKey(0)
