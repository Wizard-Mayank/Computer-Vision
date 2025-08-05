import cv2 as cv

# reading
soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

# resizing
resizedSoldiers = cv.resize(soldiers, (700, 700), interpolation=cv.INTER_AREA)
# cv.imshow("resized soldiers", resizedSoldiers)

# average blur
avgBlur = cv.blur(resizedSoldiers, (7, 7))
cv.imshow("average Blur", avgBlur)

# gaussian blur
gaussBlur = cv.GaussianBlur(resizedSoldiers, (7, 7), 0)
cv.imshow("Gaussian Blur", gaussBlur)

# median blur  (not meant for larger kSize)
median = cv.medianBlur(resizedSoldiers, 7)
cv.imshow("Median Blur", median)

# bilateral blur  (preserves edges)
bilateralBlur = cv.bilateralFilter(resizedSoldiers, 7, 10, 30)
cv.imshow("Bilateral blur", bilateralBlur)

cv.waitKey(0)
cv.destroyAllWindows()
