# OpenCV读取的格式是BGR
import cv2
import matplotlib.pyplot as plot
import numpy as np

# cv2.IMREAD_COLOR：彩色图像
# cv2.IMREAD_GRAYSCALE：灰度图像
img = cv2.imread('../image/P4_2_cat.jpg')

print(img)

# 图像的显示，也可以创建多个窗口
cv2.imshow('image', img)

# 等待时间，毫秒级，0表示任意键终止
cv2.waitKey(0)
cv2.destroyAllWindows()
