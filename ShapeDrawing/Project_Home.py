import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.rectangle(blank, (210, 250), (450, 400), (255, 255, 255), 3)  # wall

cv.rectangle(blank, (210, 250), (75, 400), (255, 255, 255), 3)  # door wall

cv.rectangle(blank, (90, 300), (195, 400), (255, 255, 255), 3)  # door frame

cv.line(blank, (90, 300), (135, 330), (255, 255, 255), 3)  # door1 upper
cv.line(blank, (195, 300), (155, 330), (255, 255, 255), 3)  # door2 upper

cv.line(blank, (135, 330), (135, 360), (255, 255, 255), 3)  # door1 mid
cv.line(blank, (155, 330), (155, 360), (255, 255, 255), 3)  # door2 mid

cv.line(blank, (135, 360), (90, 400), (255, 255, 255), 3)  # door1 lower
cv.line(blank, (155, 360), (195, 400), (255, 255, 255), 3)  # door2 lower

cv.circle(blank, (125, 345), 2, (255, 255, 255), 2)  # door1 handle
cv.circle(blank, (165, 345), 2, (255, 255, 255), 2)  # door2 handle

cv.line(blank, (75, 250), (143, 150), (255, 255, 255), 3)  # triangle left edge
cv.line(blank, (210, 250), (143, 150), (255, 255, 255), 3)  # triangle right edge

cv.line(blank, (450, 250), (383, 150), (255, 255, 255), 3)  # parallelogram right edge
cv.line(blank, (383, 150), (143, 150), (255, 255, 255), 3)  # parallelogram upper edge

cv.line(blank, (270, 150), (270, 100), (255, 255, 255), 3)  # chimney left edge
cv.line(blank, (320, 150), (320, 100), (255, 255, 255), 3)  # chimney right edge
cv.line(blank, (320, 100), (270, 100), (255, 255, 255), 3)  # chimney upper edge

cv.circle(blank, (250, 80), 5, (255, 255, 255), 2)  # smoke 1
cv.circle(blank, (220, 60), 10, (255, 255, 255), 2)  # smoke 2
cv.circle(blank, (183, 33), 17, (255, 255, 255), 2)  # smoke 3

cv.circle(blank, (143, 215), 34, (255, 255, 255), 2)  # circle within triangle

cv.line(blank, (143, 249), (143, 183), (255, 255, 255), 2)  # inside chimney line 1(vertical)
cv.line(blank, (111, 215), (175, 215), (255, 255, 255), 2)  # inside chimney line 2(horizontal)
cv.line(blank, (120, 238), (166, 192), (255, 255, 255), 2)  # inside chimney line 3(fwd slash)
cv.line(blank, (120, 192), (166, 238), (255, 255, 255), 2)  # inside chimney line 1(vertical)

cv.rectangle(blank, (240, 280), (320, 330), (255, 255, 255), 2)  # left window
cv.rectangle(blank, (340, 280), (420, 330), (255, 255, 255), 2)  # right window

cv.line(blank, (265, 280), (265, 330), (255, 255,255), 2)  # left window left pole
cv.line(blank, (295, 280), (295, 330), (255, 255,255), 2)  # left window right pole
cv.line(blank, (365, 280), (365, 330), (255, 255,255), 2)  # right window left pole
cv.line(blank, (395, 280), (395, 330), (255, 255,255), 2)  # right window right pole

cv.putText(blank, "Mayank's Hut", (160, 450), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 0), 3)  # text below hut

cv.imshow("House image", blank)

cv.waitKey(0)