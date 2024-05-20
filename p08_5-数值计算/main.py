import cv2

img_cat = cv2.imread('../image/P4_2_cat.jpg')
img_dog = cv2.imread('../image/P8_1_dog.jpg')

img_cat2 = img_cat + 10
print(img_cat[:5, :, 0])

print(img_cat2[:5, :, 0])

# 相当于%256
print((img_cat + img_cat2)[:5, :, 0])

print(cv2.add(img_cat, img_cat2)[:5, :, 0])
