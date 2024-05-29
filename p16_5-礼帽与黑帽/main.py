import cv2
import numpy as np

kernel = np.ones((7, 7), np.uint8)

# 礼帽=原始输入-开运算结果
img = cv2.imread('../image/P12_1_dige.png')
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 黑帽=闭运算-原始输入
img = cv2.imread('../image/P12_1_dige.png')
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
