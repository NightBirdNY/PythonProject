import cv2 as cv

#reading images

#img = cv.imread('OPEN_CV/Photos/cat1.jpeg')
#cv.imshow('Cat', img)

#reading videos

capture = cv.VideoCapture('OPEN_CV/Photos/random.mp4') # 0 for webcam access
while True:
    isTrue, frame = capture.read() #frame by frame reading and return true if video is not ended
    # If video ended replay
    if not isTrue:
        capture.set(cv.CAP_PROP_POS_FRAMES, 0)
        continue
    cv.imshow('Video', frame) #shows a window named video
    if cv.waitKey(20) & 0xFF == ord('d'): # press d for close the window
        break
capture.release()
cv.destroyAllWindows()
