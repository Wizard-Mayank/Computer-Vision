import cv2 as cv
import numpy as np

# reading
soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

# resizing
resizedSoldiers = cv.resize(soldiers, (700, 700), interpolation=cv.INTER_AREA)
cv.imshow("resized soldiers", resizedSoldiers)

# blank black image
blank = np.zeros(resizedSoldiers.shape[:2], dtype="uint8")

# splitting
b, g, r = cv.split(resizedSoldiers)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

# dimensions of each
print(resizedSoldiers.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging (only 1 channel available, images appear in grayscale)
mergedSoldiers = cv.merge([b, g, r])
cv.imshow("Merged Soldeirs", mergedSoldiers)

# merging (all 3 channels available, images appear in bgr)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

cv.waitKey(0)
cv.destroyAllWindows()
