import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


img = cv2.imread('../image/P4_2_cat.jpg')
cat = img[0:200, 0:200]
cv_show('cat', cat)

# 颜色通道提取
b, g, r = cv2.split(img)
print(b)
print(b.shape)

img = cv2.merge((b, g, r))
print(img.shape)

# 只保留R
cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 1] = 0
cv_show('R', cur_img)

# 只保留G
cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 2] = 0
cv_show('G', cur_img)

# 只保留B
cur_img = img.copy()
cur_img[:, :, 1] = 0
cur_img[:, :, 2] = 0
cv_show('B', cur_img)
