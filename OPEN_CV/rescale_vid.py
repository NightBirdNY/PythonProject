
import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int (frame.shape[1]*scale)
    height = int (frame.shape[0]*scale)

    dimensions = (width, height)
    return cv.resize(frame,dimensions ,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0) # 0 for webcam access
while True:
    isTrue, frame = capture.read() #frame by frame reading and return true if video is not ended
    frame_resize = rescaleFrame(frame, scale=0.3)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)#shows a window named video
    if cv.waitKey(20) & 0xFF == ord('d'): # press d for close the window
        break
capture.release()
cv.destroyAllWindows()