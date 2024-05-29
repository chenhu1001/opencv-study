import cv2
import numpy as np

# 开：先腐蚀，再膨胀
img = cv2.imread('../image/P12_1_dige.png')

kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('opening', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 闭：先膨胀， 在腐蚀
img = cv2.imread('../image/P12_1_dige.png')

kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
