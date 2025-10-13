import cv2 as cv
import numpy as np

img = cv.imread('OPEN_CV/Photos/OPEN_CV_test.png')
resized = cv.resize(img, (600, 450))
cv.imshow('Original', resized)

#split
b,g,r = cv.split(resized)
blank=np.zeros(img.shape[:2], dtype='uint8')

#Splited and merged images for human eye splited image
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

#splited images in value
cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)

#splited and merged images in bgr
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

#Printing shape values
print(resized.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)