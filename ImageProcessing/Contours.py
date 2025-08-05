import cv2 as cv
import numpy as np

soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

resizedSoldiers = cv.resize(soldiers, (800, 700), interpolation=cv.INTER_AREA)
# cv.imshow("Resized soldiers", resizedSoldiers)

graySoldiers = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray soldiers", graySoldiers)

blurredGraySoldiers = cv.GaussianBlur(graySoldiers, (3, 3), 100)
# # cv.imshow("Blurred gray soldiers", blurredGraySoldiers)

# finding canny                                                    ''' method 1 (recommended)'''
CannySoldiers = cv.Canny(blurredGraySoldiers, 50, 255)
cv.imshow("Soldiers canny", CannySoldiers)

# dilatedSoldiers = cv.dilate(CannySoldiers, (3, 3), iterations=1)
# # cv.imshow("Dilated Soldiers", dilatedSoldiers)

# ErodedSoldiers = cv.erode(dilatedSoldiers, (3, 3), iterations=1)
# cv.imshow("Eroded Soldiers", ErodedSoldiers)

# binarizing the image                                              ''' method 2'''
# ret, thresh = cv.threshold(graySoldiers, 100, 255, cv.THRESH_BINARY)
# cv.imshow("Binarized soldiers", thresh)

# blurredBinarizedSoldiers = cv.GaussianBlur(thresh, (3, 3), 100)
# cv.imshow("Blurred binarized soldiers", blurredBinarizedSoldiers)

# finding contours
soldiersContours, hierarchy = cv.findContours(
    CannySoldiers, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE
)
print(f"{len(soldiersContours)} countours found having hierarchy : \n {hierarchy}")

# blank black image
blank = np.zeros(resizedSoldiers.shape, dtype="uint8")
# cv.imshow("Blank", blank)

# drawing contours
cv.drawContours(blank, soldiersContours, -1, (0, 0, 255), 1)
cv.imshow("Contours drawn", blank)

cv.waitKey(0)
