import cv2 as cv

img = cv.imread('OPEN_CV/Photos/cat1.jpeg')

def rescaleFrame(frame, scale= 0.1):
     #channel =int(frame.shape[2]) #channel number (RGB)
     width = int(frame.shape[1] * scale)
     height = int(frame.shape[0] * scale)
     dimension = (width, height)

     return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Resized Image', resized_image)
cv.waitKey(0)