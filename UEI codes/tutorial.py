import cv2
import numpy as np

image= cv2.imread("images/pinapple.jpg")

print(type(image))
print(image.shape)
# print(image)

cv2.imshow("window",image)

cv2.waitKey(10000)

