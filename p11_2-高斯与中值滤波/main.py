import cv2
import numpy as np

img = cv2.imread('../image/P10_2_LenaNoise.png')

# 高斯滤波
# 高斯模糊的卷积核里的数值满足高斯分布， 相当于更重视中间的
gaussian = cv2.GaussianBlur(img, (5, 5), 1)

cv2.imshow('gaussian', gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 中值滤波
# 相当于用中值代替
median = cv2.medianBlur(img, 5)  # 中值滤波

cv2.imshow('median', median)
cv2.waitKey(0)
cv2.destroyAllWindows()

res = np.hstack((gaussian, median))
print(res)
cv2.imshow('gaussian vs median', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
