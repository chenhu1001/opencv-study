import cv2

img = cv2.imread('../image/P12_2_pie.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# dst = cv2.Sobel(src, ddepth, dx, dy, ksize)
# ddepth：图像的深度
# dx和dy分别表示水平和竖直方向
# ksize是Sobel算子的大小

def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# 白到黑是正数，黑到白就是负数了，所有的负数会被截断成0，所以要取绝对值
cv_show(sobelx, 'sobelx')
