import cv2 as cv

# video to read
friends = cv.VideoCapture(
    "E:\Python Projects\Computer_Vision\Assets\Videos\Friends.mp4"
)

# face detector classifier
classifier = cv.CascadeClassifier(
    "E:\Python Projects\Computer_Vision\Face Detection and Recognition\haar_face.xml"
)


# resizing the frame
def resizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dims = (width, height)

    return cv.resize(frame, dims, interpolation=cv.INTER_AREA)


# finding faces in a frame using haar cascade
def findFaces(frame):
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = classifier.detectMultiScale(frame, 1.1, 3)

    print(f"Number of faces : {len(faces_rect)}")

    for x, y, w, h in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


# reading, resizing and finding faces in the video frame by frame
while True:
    isTrue, frame = friends.read()

    resizedFrame = resizeFrame(frame, 0.25)

    findFaces(resizedFrame)

    cv.imshow("Resized Friends", resizedFrame)

    if cv.waitKey(1) & 0xFF == ord("s"):
        break

friends.release()
cv.destroyAllWindows()
