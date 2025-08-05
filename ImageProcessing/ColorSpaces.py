import cv2 as cv
import matplotlib.pyplot as plt

soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

resizedSoldiers = cv.resize(soldiers, (800, 700), interpolation=cv.INTER_AREA)
cv.imshow("Resized soldiers", resizedSoldiers)

soldiersRGB = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2RGB)
cv.imshow("RGB Soldiers", soldiersRGB)

resizedSoldiersRGB = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2RGB)
cv.imshow("Soldeirs RGB", resizedSoldiersRGB)

plt.imshow(soldiersRGB)
plt.show()

# # grayscale
# graySoldiers = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray soldiers", graySoldiers)

# # hsv
# hsvSoldiers = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2HSV)
# cv.imshow("HSV soldiers", hsvSoldiers)

# # l*a*b         ''' more like how humans percieve colors
# labSoldiers = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2LAB)
# cv.imshow("HSV soldiers", labSoldiers)

cv.waitKey(0)
cv.destroyAllWindows()
