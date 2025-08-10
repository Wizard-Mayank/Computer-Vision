import cv2 as cv

children = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\children.jpg")
# cv.imshow("Children", children)

resizedChildren = cv.resize(children, (850, 700), interpolation=cv.INTER_AREA)
cv.imshow("Resized children", resizedChildren)

# blurring image to minimize noise
blurredChildren = cv.GaussianBlur(resizedChildren, (5, 5), 1)
cv.imshow("Blurred children", blurredChildren)

# converting to gray scale for face detection
grayChildren = cv.cvtColor(blurredChildren, cv.COLOR_BGR2GRAY)
cv.imshow("Gray children", grayChildren)

# making classifier ready to use
haar_cascade = cv.CascadeClassifier(
    "E:\Python Projects\Computer_Vision\Face Detection and Recognition\haar_face.xml"
)

# getting a list of rectangles for the faces in (x, y, w, h) format of each elem
faces_rect = haar_cascade.detectMultiScale(grayChildren, 1.1, 2)
print(f"Number of faces: {len(faces_rect)}")

# drawing rectangles around faces in the image
for x, y, w, h in faces_rect:
    cv.rectangle(resizedChildren, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv.imshow("Faces detected", resizedChildren)

cv.waitKey(0)
cv.destroyAllWindows()
