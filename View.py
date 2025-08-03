import cv2 as cv

# Selecting and viewing Image
# myImg = cv.imread("E:\Python Projects\Computer_Vision\Images\Mayank.jpg")
# cv.imshow("Myself", myImg)
# print(myImg.shape)

# Selecting the video
capture = cv.VideoCapture("Computer_Vision\Videos\Doggy.mp4")

# Viewing selected video
while True:
       isTrue, frame = capture.read()
        
       cv.imshow("Dog Video", frame)
        
       if cv.waitKey(1) & 0xFF==ord('s'):  # stop the video when s is pressed
           break

# Releasing pointer and closing all windows  
capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)
