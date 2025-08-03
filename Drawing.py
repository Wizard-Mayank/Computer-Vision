import cv2 as cv
import numpy as np

# create a black blank img
blank = np.zeros((500, 500, 3), dtype='uint8')

# cv.imshow("Blank Image", blank)

# # color the image
# blank[0:300, 200:300] = 0, 0, 255
# cv.imshow("Red rectangle inside the Image", blank)

# # draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), 2)
# cv.imshow("Rectangle inside the Image", blank)

# draw a circle
# cv.circle(blank, (250, 250), 250, (0, 0, 255), 3)
# cv.imshow("Circle", blank)

# draw a line
cv.line(blank, (250, 10), (250, 250), (0, 0, 255), 4)
cv.imshow("Line", blank)

cv.waitKey(0)