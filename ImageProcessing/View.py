import cv2 as cv

# Selecting and viewing Image
myImg = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Mayank.jpg")
cv.imshow("Myself", myImg)
print(myImg.shape)


cv.waitKey(0)
