import cv2 as cv
import matplotlib.pyplot as plt

# reading
soldiers = cv.imread("E:\Python Projects\Computer_Vision\Assets\Images\Soldiers.jpg")
# cv.imshow("Soldiers", soldiers)

# resizing
resizedSoldiers = cv.resize(soldiers, (700, 600), interpolation=cv.INTER_AREA)
cv.imshow("resized soldiers", resizedSoldiers)

# transforming to grayscale img
# graySoldiers = cv.cvtColor(resizedSoldiers, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", graySoldiers)

# threshold, thresh = cv.threshold(graySoldiers, 100, 255, cv.THRESH_BINARY)
# cv.imshow("Binarized", thresh)

# histo = cv.calcHist(graySoldiers, [0], None, [256], [0, 256])  # binary color histogram

# plt.figure()
# plt.title("Pixels Histogram")
# plt.xlabel("Pixels Range")
# plt.ylabel("Pixel Intensity")
# plt.xlim([0, 256])
# plt.plot(histo)
# plt.show()

colors = ["b", "g", "r"]

plt.figure()
plt.title("Color Pixels Histogram")
plt.xlabel("Pixels Range")
plt.ylabel("Pixel Intensity")
plt.xlim([0, 256])

for i, col in enumerate(colors):
    colorHisto = cv.calcHist(
        resizedSoldiers, [i], None, [256], [0, 256]
    )  # color histogram
    plt.plot(colorHisto, color=col)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
