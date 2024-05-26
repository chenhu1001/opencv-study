import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


img = cv2.imread('../image/P10_2_LenaNoise.png')
cv_show('img', img)

# 均值滤波
# 简单的平均卷积操作
blur = cv2.blur(img, (3, 3))
cv_show('blur', blur)

# 方框滤波
# 基本和均值一样， 可以选择归一化
box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
cv_show('box', box)

# 方框滤波
# 基本和均值一样， 可以选择归一化
box = cv2.boxFilter(img, -1, (3, 3), normalize=False)
cv_show('box', box)
