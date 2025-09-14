import cv2 as cv

img = cv.imread('OPEN_CV/Photos/cat3.jpeg')
cv.imshow('Cat', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#Blur edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Blur', canny)

#Dilating the image
dilated = cv.dilate(canny,(3,3), iterations=1)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(canny,(3,3), iterations=1)
cv.imshow('Eroded', eroded)

#Resize but Scaling distortion
resized = cv.resize(img,(480,480),cv.INTER_LANCZOS4)
cv.imshow('Resized', resized)

#Croping
cropped = img [50:200,300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)