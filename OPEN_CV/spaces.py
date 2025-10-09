import cv2 as cv

#Color spaces

img = cv.imread('OPEN_CV/Photos/cat3.jpeg')
height, width = img.shape[:2]
print(height, width)
aspect_ratio = width / height
print(aspect_ratio)
resized = cv.resize(img, (600, 450))
cv.imshow('Original', resized)

#BGR to Grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV (HUE-saturation-value)
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to LAB (Light green-red yellow-blue)
lab= cv.cvtColor(resized, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb= cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)