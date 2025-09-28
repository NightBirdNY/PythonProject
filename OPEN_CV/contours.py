import cv2 as cv

img = cv.imread('OPEN_CV/Photos/cat3.jpeg')

cv.imshow('Original', img)
#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
#Contours
canny = cv.Canny(gray, 50, 150)
cv.imshow('Canny', canny)


contours, hierarchies=cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

cv.waitKey(0)