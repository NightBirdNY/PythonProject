#Drawing R, G , B and K 500*500 windows
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#1.black
cv.imshow('Blank', blank)
#2.RGB
blank[:] = 0,250,0
cv.imshow('Green', blank)
blank[:] = 0,0,255
cv.imshow('RED', blank)
blank[:] = 255,0,0
cv.imshow('Blue', blank)

#3.rectangle
blank[:] = 0,0,0
#Start from origin which is top left of image and drawing 2 px line 250*250
cv.rectangle(blank,(0,0),(250,250),(255,255,255),thickness=-1)
# cv.FILLED or -1 for fill inside
# can use (blank.shape[1]//2, blank.shape [0]//2) instead of (250,250)
cv.imshow('rectangle', blank)

#4.circle
blank[:] = 0,0,0
cv.circle(blank,(250,250),50,(255,255,255),thickness=-1)
#(250,250) is center and 50 is radius last () is color
cv.imshow('circle', blank)

#5. line
blank[:] = 0,0,0
cv.line(blank,(0,250),(500,250),(255,255,255),thickness=12)

cv.imshow('line', blank)

#6.Text
blank[:] = 0,0,0
cv.putText(blank, 'Hello',(255,250), cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
cv.putText(blank, 'world',(255,300), cv.FONT_ITALIC,1.0,(255,255,255),thickness=2)

cv.imshow('text', blank)
cv.waitKey(0)