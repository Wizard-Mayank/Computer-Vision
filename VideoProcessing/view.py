import cv2 as cv

# Selecting the video
capture = cv.VideoCapture("E:\Python Projects\Computer_Vision\Assets\Videos\Doggy.mp4")

# Viewing selected video
while True:
       isTrue, frame = capture.read()
        
       cv.imshow("Dog Video", frame)
        
       if cv.waitKey(1) & 0xFF==ord('s'):  # stop the video when s is pressed
           break

# Releasing pointer and closing all windows  
capture.release()
cv.destroyAllWindows()