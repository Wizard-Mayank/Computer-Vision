import cv2 as cv
import numpy as np

# reading
soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

# resizing
resizedSoldiers = cv.resize(soldiers, (700, 700), interpolation=cv.INTER_AREA)
cv.imshow("resized soldiers", resizedSoldiers)

# blank black image
blank = np.zeros((700, 700), dtype="uint8")
# cv.imshow("Blank image", blank)

# circle
mask = cv.circle(
    blank.copy(),
    (blank.shape[1] // 2, blank.shape[0] // 2 - 150),
    100,
    255,
    -1,
)
# cv.imshow("Mask", mask)

maskedSoldiers = cv.bitwise_and(resizedSoldiers, resizedSoldiers, mask=mask)
cv.imshow("Masked Soldiers", maskedSoldiers)

cv.waitKey(0)
cv.destroyAllWindows()
