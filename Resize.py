import cv2 as cv

# Selecting and viewing Image
# myImg = cv.imread("Computer_Vision\Images\Mayank.jpg")
# cv.imshow("Myself", myImg)

# Selecting the video
capture = cv.VideoCapture("Computer_Vision\Videos\Doggy.mp4")

# Resizing the frame
def resizeFrame(frame, scale=0.75):
    # works for standalone files(imgs, vids, live)
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#Resizing the frame
# def changeRes(height, width):
#     # live video
#     capture.set(3, height)
#     capture.set(4, width)

# Viewing selected video
while True:
        isTrue, frame = capture.read()
        resizedFrame = resizeFrame(frame, 0.25)
        
        cv.imshow("Video Resized", resizedFrame)
        
        if cv.waitKey(1) & 0xFF==ord('s'):  # stop the video when s is pressed
            break

# Releasing pointer and closing all windows  
capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)