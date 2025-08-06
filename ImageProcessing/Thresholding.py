import cv2 as cv

# reading
soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

# resizing
resizedSoldiers = cv.resize(soldiers, (700, 600), interpolation=cv.INTER_AREA)
# cv.imshow("resized soldiers", resizedSoldiers)

# transforming to grayscale img
graySoldiers = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", graySoldiers)

# binarizing the img
threshold, thresh = cv.threshold(graySoldiers, 100, 255, cv.THRESH_BINARY)
cv.imshow("Binarized", thresh)


# inverse binarizing the img
threshold, thresh_inv = cv.threshold(graySoldiers, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("Inverse Binarized", thresh_inv)

# adaptive binarizing the img
adapThresh = cv.adaptiveThreshold(
    graySoldiers, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2
)
cv.imshow("Binarized", adapThresh)

cv.waitKey(0)
cv.destroyAllWindows()
