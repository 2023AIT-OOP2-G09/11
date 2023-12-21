import cv2
import numpy as np

img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
dst = cv2.Canny(gray, 100, 200)
cv2.imwrite("output.jpg", dst)