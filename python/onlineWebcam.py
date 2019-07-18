import urllib.request
import cv2
import numpy as np

url = input("Enter URL : ")    # Using ipwebcam app download it from play store https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN
print("Starting")
while True:
  imgResp = urllib.request.urlopen(url)
  imgNp = np.array(bytearray(imgResp.read()), np.uint8)
  img = cv2.imdecode(imgNp, -1)
  cv2.imshow("Online webcam", img)
cv2.destroyAllWindows()
 
