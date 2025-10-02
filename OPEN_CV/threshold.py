import cv2 as cv
import numpy as np
#Original image
img = cv.imread('OPEN_CV/Photos/cat3.jpeg')
cv.imshow('Original', img)

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Blank
blank= np.zeros(resized.shape,dtype="uint8")
cv.imshow('Blank', blank)

#Grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Binarize/ threshold
ret,thresh= cv.threshold( gray,125,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow('Threshold', thresh)

#Counting contours
contours, hierarchies=cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

#Contour drawing
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

#Canny and Threshold comp
canny = cv.Canny(gray, 50, 150)
cv.imshow('Canny', canny)

#Countour drawing on original image
cv.drawContours(resized, contours, -1, (0,0,255), 1)
cv.imshow("Contours on Original", resized)

cv.waitKey(0)