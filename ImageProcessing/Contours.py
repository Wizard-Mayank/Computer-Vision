import cv2 as cv

soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

resizedSoldiers = cv.resize(soldiers, (800, 700), interpolation=cv.INTER_AREA)
cv.imshow("Resized soldiers", resizedSoldiers)

cv.waitKey(0)