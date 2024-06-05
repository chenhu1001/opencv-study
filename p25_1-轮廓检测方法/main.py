# cv2.findContours(img,mode,method)

# mode：轮廓检测模式

# RETR_EXTERNAL：只检索最外面的轮廓；
# RETR_LIST：检索所有的轮廓，并将其保存在一条链表当中；
# RETR_CCOMP：检索所有的轮廓，并将他们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界；
# RETR_TREE：检索所有的轮廓，并重构嵌套轮廓的整个层次；
# method：轮廓逼近方法

# CHAIN_APPROX_NONE：以Freeman链码方式输出轮廓，所有其他方法输出多边形（顶点的序列）。
# CHAIN_APPROX_SIMPLE：压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分。

import cv2


def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


img = cv2.imread('../image/P22_2_car.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv_show(thresh, 'thresh')

# 在opencv-python 4.4.0版本中，此函数返回值只有两个
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)