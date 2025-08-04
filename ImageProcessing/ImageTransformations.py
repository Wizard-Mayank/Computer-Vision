import cv2 as cv
import numpy as np

soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

# resizing the img
resizedSoldiers = cv.resize(soldiers, (700, 600), interpolation=cv.INTER_AREA)
cv.imshow("resized Soldiers", resizedSoldiers)


# to shift(translate) image in any direction -x = Left, +x = R, -y = U, +y = Down
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# shifting img towards Top Left corner
# translatedSoldiers = translate(resizedSoldiers, -300, -100)
# cv.imshow("Translated soldiers", translatedSoldiers)


# to rotate image -angle = clockwise +angle = counter-clockwise
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotatedSoldiers1 = rotate(resizedSoldiers, -45)
cv.imshow("Rotated Soldiers 1", rotatedSoldiers1)

# rotatedSoldiers2 = rotate(rotatedSoldiers1, -45)
# cv.imshow("Rotated Soldiers 2", rotatedSoldiers2)

# fliping the image    0=vertically, 1=horizontally, -1=both
flippedSoldiers = cv.flip(resizedSoldiers, -1)
cv.imshow("Flipped soldiers", flippedSoldiers)

# cropping the image
croppedSoldiers = resizedSoldiers[100:300, 300:600]
cv.imshow("Cropped Soldiers", croppedSoldiers)

cv.waitKey(0)
