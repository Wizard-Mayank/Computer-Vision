import cv2 as cv
import numpy as np

# blank black image
blank = np.zeros((500, 500), dtype="uint8")
# cv.imshow("Blank image", blank)

# rectangle
rectangle = cv.rectangle(blank.copy(), (30, 30), (470, 470), 255, -1)
cv.imshow("Rectangle", rectangle)

# circle
circle = cv.circle(blank.copy(), (250, 250), 240, 255, -1)
cv.imshow("Circle", circle)

# bitwise_and --> intersection area
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_and", bitwise_and)

# bitwise_or --> non-intersection and intersection area
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)

# bitwise_xor --> non-intersection area
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)

# bitwise_not --> inverts image color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise_not", bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()
