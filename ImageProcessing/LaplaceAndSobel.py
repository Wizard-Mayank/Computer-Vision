import cv2 as cv
import numpy as np

# reading
nature = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\\Nature.jpg")
# cv.imshow("nature", nature)

# resizing
resizedNature = cv.resize(nature, (700, 600), interpolation=cv.INTER_AREA)
cv.imshow("resized nature", resizedNature)

# creating a black image
# blank = np.zeros(resizedNature.shape[:2], dtype="uint8")

# splitting to 3 color channels
# b, g, r = cv.split(resizedNature)
# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)

# merging with blank to get only blue color channel
# blue = cv.merge([b, blank, blank])
# cv.imshow("BLUE", blue)

# blurring nature
# blurredNature = cv.GaussianBlur(resizedNature, (3, 3), 100)
# cv.imshow("Blurred nature", blurredNature)

# converting bgr2gray scale
grayNature = cv.cvtColor(resizedNature, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray nature", grayNature)

# finding gradients using Laplacian()
laplacianNature = cv.Laplacian(grayNature, cv.CV_64F)  # CV_64F to prevent overflowing
laplacianNature = np.uint8(
    np.absolute(laplacianNature)
)  # removing -ve values and then converting in the scale of [0, 255]
cv.imshow("Laplacian nature", laplacianNature)

# finding gradients using sobel
sobelX = cv.Sobel(grayNature, cv.CV_64F, 1, 0)  # along x axis
sobelY = cv.Sobel(grayNature, cv.CV_64F, 0, 1)  # along y axis
combinedSobel = cv.bitwise_or(sobelX, sobelY)  # combining both

# cv.imshow("SobelX", sobelX)
# cv.imshow("SobelY", sobelY)
cv.imshow("Combined Sobel", combinedSobel)

# finding edges using canny which is a multistep process having Sobel as one of its phase
canny = cv.Canny(grayNature, 100, 255)
cv.imshow("Canny", canny)

cv.waitKey(0)
cv.destroyAllWindows()
