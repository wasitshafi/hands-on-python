import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

dataPath ="dataset/"
onlyFiles = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]
trainingData, labels = [], []

for i, files in enumerate(onlyFiles):
     imagePath = dataPath + onlyFiles[i]
     images = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
     trainingData.append(np.asarray(images, dtype= np.uint8))
     labels.append(i)
     
labels = np.asarray(labels, dtype= np.int32)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(trainingData), np.asarray(labels))
print ("Model Training Complete....!")
