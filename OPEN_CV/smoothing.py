import cv2 as cv

img = cv.imread('OPEN_CV/Photos/OPEN_CV_test.png')
cv.imshow('OpenCV', img)

#Averaging
average = cv.blur(img, (5,5))
cv.imshow('Blur', average)

#Gaussian
gaussian = cv.GaussianBlur(average, (5,5), 0)
cv.imshow('Gaussian', gaussian)

#Median
median = cv.medianBlur(average, 5)
cv.imshow('Median', median)

#Bilateral
bilateral = cv.bilateralFilter(average, 5, 15, 15)
#parameteres : 1. src = image, 2. d= distance for near pixel, 3. sigmacolor= color similarity  ,4.sigmaspace=  filter sigma
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)