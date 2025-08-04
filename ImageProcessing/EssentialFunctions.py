import cv2 as cv

soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)


# resizing soldiers image
def resizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resizedSoldiers = resizeFrame(soldiers, 0.22)

# cv.imshow("Resized soldiers", resizedSoldiers)

# converting bgr image to grayscale
grayScaleSoldiers = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray scale soldiers:", grayScaleSoldiers)

# blurring grayscale image using gaussian blur
blurredSoldiers = cv.GaussianBlur(grayScaleSoldiers, (3, 3), 100)
# cv.imshow("Blurred soldiers canny", blurredSoldiers)

# finding out edges of blurred image using Canny
soldiersCanny = cv.Canny(blurredSoldiers, 100, 200)
cv.imshow("Soldiers canny:", soldiersCanny)

# dilating (expanding white pixels) the image
dilatedSoldiers = cv.dilate(soldiersCanny, (3, 3), iterations=1)
cv.imshow("Dilated Soldiers", dilatedSoldiers)

# eroding (shrinking white pixels) the image
erodedSoldiers = cv.erode(dilatedSoldiers, (3, 3), iterations=1)
cv.imshow("Eroded soldiers", erodedSoldiers)

# resizing soldiers
# resizedSoldiers = cv.resize(erodedSoldiers, (500, 500), interpolation=cv.INTER_AREA)
# cv.imshow("Resized Soldiers", resizedSoldiers)

# cropping soldiers
# croppedSoldiers = erodedSoldiers[10:300, 300:500]
# cv.imshow("Cropped Soldiers", croppedSoldiers)

cv.waitKey(0)
cv.destroyAllWindows()
