import cv2
import matplotlib.pyplot as plt


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


img_cat = cv2.imread('../image/P4_2_cat.jpg')
img_dog = cv2.imread('../image/P8_1_dog.jpg')

img_cat2 = img_cat + 10
print(img_cat[:5, :, 0])

print(img_cat2[:5, :, 0])

# 相当于%256
print((img_cat + img_cat2)[:5, :, 0])

print(cv2.add(img_cat, img_cat2)[:5, :, 0])

# 图像融合
print(img_cat.shape)
print(img_dog.shape)

img_dog = cv2.resize(img_dog, (500, 414))
print(img_dog.shape)

# 对两幅图像进行加权混合，得到一幅新的图像。
res = cv2.addWeighted(img_cat, 0.4, img_dog, 0.6, 0)
cv_show('res', res)

# 将图像宽度缩放为原来的 3 倍，高度保持不变。
res = cv2.resize(img_cat, (0, 0), fx=3, fy=1)
cv_show('res', res)

# 将图像高度缩放为原来的 3 倍，宽度保持不变。
res = cv2.resize(img_cat, (0, 0), fx=1, fy=3)
cv_show('res', res)
