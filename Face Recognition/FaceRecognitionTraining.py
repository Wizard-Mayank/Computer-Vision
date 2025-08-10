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
DIR = r"F:\Face Recognition\training data"

# load the haar cascade classifier
classifier = cv.CascadeClassifier(
    "E:\Python Projects\Computer_Vision\Face Detection and Recognition\haar_face.xml"
)

# mapped data will be stored on these lists for the model to train
features = []
labels = []


def train_model():
    for person in people:  # pick a person
        path = os.path.join(DIR, person)  # get that person's path
        label = people.index(person)  # get index of that person

        for img in os.listdir(path):  # iterate over each img of that person

            person_img = cv.imread(os.path.join(path, img))  # get person's img

            gray_img = cv.cvtColor(
                person_img, cv.COLOR_BGR2GRAY
            )  # convert to grayscale

            faces_rect = classifier.detectMultiScale(
                gray_img, 1.5, 4
            )  # detect face of that person using haar cascade

            for x, y, w, h in faces_rect:
                face_roi = gray_img[
                    y : y + h, x : x + w
                ]  # person's region of interest through cropping

                cv.imshow("Region of interest", face_roi)

                cv.waitKey(0)

                features.append(face_roi)  # store person's face matrix
                labels.append(label)  # store person's face label


train_model()  # start training

# length of data
print(f"Length of features : {len(features)}.")
print(f"Length of labels : {len(labels)}.")
