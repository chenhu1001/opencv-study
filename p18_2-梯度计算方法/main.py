import cv2

img = cv2.imread('../image/P12_2_pie.png', cv2.IMREAD_GRAYSCALE)


def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
cv_show(sobelx, 'sobelx')

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
cv_show(sobely, 'sobely')

# 分别计算x和y，再求和
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
sobelxy = cv2.convertScaleAbs(sobelxy)
cv_show(sobelxy, 'sobelxy')

# 不建议直接计算
sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
sobelxy = cv2.convertScaleAbs(sobelxy)
cv_show(sobelxy, 'sobelxy')

img = cv2.imread('../image/P18_1_Lena.jpg', cv2.IMREAD_GRAYSCALE)
cv_show(img, 'img')

img = cv2.imread('../image/P18_1_Lena.jpg', cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv_show(sobelxy, 'sobelxy')

img = cv2.imread('../image/P18_1_Lena.jpg', cv2.IMREAD_GRAYSCALE)

sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
sobelxy = cv2.convertScaleAbs(sobelxy)
cv_show(sobelxy, 'sobelxy')
