import cv2 as cv
import os
import numpy as np

# Method 1 -> manually type

# Method 2
people = []
for i in os.listdir(r"F:\Face Recognition\training data"):
    people.append(i)
# print(people)

# parent directory
DIR = r'F:\Face Recognition\training data'

# load the haar cascade classifier
classifier = cv.CascadeClassifier("E:\Python Projects\Computer_Vision\Face Detection and Recognition\haar_face.xml")

# mapped data will be stored on these lists for the model to train
features = []
label = []

def train_model():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        path_img = cv.imread(path)
        gray_img = cv.cvtColor(path_img, cv.COLOR_BGR2GRAY)
        
        