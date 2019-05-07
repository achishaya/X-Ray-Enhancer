import cv2
import numpy as np

#Method One - Thresholding

img = cv2.imread('xray.jpg') #enter image name and type
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 115, 1)
median2 = cv2.medianBlur(gaus,15)

#output
#cv2.imshow('Input', img)
#cv2.imshow('Thresholding Output', median2)
#cv2.imshow('Convert Color', grayscaled)
#cv2.imshow('Adaptive Threshold Gaussian', gaus)

#Using color filtering method


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_filter = np.array([0, 0, 0])
upper_filter = np.array([255, 255, 255])

mask = cv2.inRange(hsv, lower_filter, upper_filter)
res = cv2.bitwise_and(img, img, mask = mask)


kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(mask, kernel, iterations = 1)

smoothed = cv2.filter2D(gaus, -1, kernel)
median = cv2.medianBlur(erosion,15)

#output

cv2.imshow('Input', img)
cv2.imshow('Color Filtering', median)




cv2.waitKey(3000000)
cv2.destroyAllWindows()
