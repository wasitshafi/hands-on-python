import cv2

file_name = "airplane.png"
img_gray_original = cv2.imread(file_name, 0)
img_gray = img_gray_original.copy()

for i in range(len(img_gray)):
    for j in range(len(img_gray[i])):
        print(img_gray[i][j])
        if img_gray[i][j] < 128:
            img_gray[i][j] = 0
        else:
            img_gray[i][j] = 255

cv2.imshow("Original Grayscale Image", img_gray_original)
cv2.imshow("Threshold Image (Similar to binary image))", img_gray)

key = cv2.waitKey(0)
cv2.destroyAllWindows()