import cv2 as cv
import numpy as np
import os

# features = np.load(r"E:\Python Projects\features.npy", allow_pickle=True)
# labels = np.load(r"E:\Python Projects\labels.npy", allow_pickle=True)

people = []
for i in os.listdir(r"F:\Face Recognition\training data"):
    people.append(i)

testing_DIR = r"F:\Face Recognition\testing data"

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read(r"E:\Python Projects\face_trained.yml")

# load the haar cascade classifier
classifier = cv.CascadeClassifier(
    r"E:\Python Projects\Computer_Vision\Face Detection\haar_face.xml"
)

for img in os.listdir(testing_DIR):
    img_path = os.path.join(testing_DIR, img)

    # print(img_path)

    test_img = cv.imread(img_path)

    gray = cv.cvtColor(test_img, cv.COLOR_BGR2GRAY)

    faces_rect = classifier.detectMultiScale(gray, 1.5, 4)

    for x, y, w, h in faces_rect:
        face_roi = gray[y : y + h, x : x + w]

        label, confidence = face_recognizer.predict(face_roi)

        print(f"Person : {people[label]} Confidence : {confidence}.")

        cv.putText(
            test_img,
            str(people[label]),
            (10, 20),
            cv.FONT_HERSHEY_COMPLEX,
            1.0,
            (0, 255, 0),
            3,
        )

        cv.rectangle(test_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv.imshow("Prediction", test_img)
        cv.waitKey(0)
        cv.destroyAllWindows()
