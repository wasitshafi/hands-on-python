import numpy as np
import cv2
import os
from PIL import Image #CTM : uppercase 'I'

recognizer = cv2.face.LBPHFaceRecognizer_create()



path = "dataSet"

def getImagesWithId(path):
    allImagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = [] #empty array
    ids = []
    for imagePath in allImagePaths:
    #for more info about Image.open() read :  https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
        faceImage = Image.open(imagePath).convert("L") # 'l is used to make image grayscale...although in this example we store the images in gray scale mode but in case we have colored image of face then it used to handle those images.....
        faceNp =np.array(faceImage, "uint8") #convert that faceimage into numpy image matrix
        id = int(os.path.split(imagePath)[-1].split("_")[1])
        faces.append(faceNp)
        print (id)
        ids.append(id)
        cv2.imshow("Training", faceNp)
        cv2.waitKey(10)
    return ids, faces

ids, faces = getImagesWithId(path)
recognizer.train(faces,np.array(ids))
recognizer.save('trainningData.yml')
cv2.destroyAllWindows()
