import cv2 as cv
import numpy as np

img = cv.imread('OPEN_CV/Photos/cat2.jpeg')

cv.imshow('Original', img)

#Translations
def trnaslate(img,x,y) :
     transMat = np.float32([[1,0,x],[0,1,y]])
     dimensions = (img.shape[1],img.shape[0])
     return cv.warpAffine(img,transMat,dimensions)

# -x ---> Left
#-y ---> Up
#x ---> Right
#y ---> Down
translated = trnaslate(img, -100,100)
cv.imshow('translated', translated)

#Rotations
def rotate(img,angle, rotPoint= None) :
    # This part gets the height and width of the image
    (height, width) = img.shape[:2]

#rotPoint is the middle pixel of the image
    if rotPoint is None :
        rotPoint = (width/2, height/2)

    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated = rotate(img, 45 )
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45 )
cv.imshow('Rotated Rotated', rotated_rotated)

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flip

#For flipping x axis
flip = cv.flip(resized,0)
cv.imshow('Bottom', flip)
#For flipping y axis
flipped = cv.flip(resized,1)
cv.imshow('Left', flipped)
#Both x and y axis
flipped = cv.flip(resized,-1)
cv.imshow('Left Bottom', flipped)

#Cropping
cropped = resized[200:400,200:400]
cv.imshow('Cropped', cropped)
# Resizeable Window
cv.namedWindow('SimpleWindow', cv.WINDOW_NORMAL)
cv.imshow('SimpleWindow', img)


cv.waitKey(0)