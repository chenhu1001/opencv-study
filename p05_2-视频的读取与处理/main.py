import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img1 = cv2.imread('../image/P4_2_cat.jpg')
print(img1.shape)

img2 = cv2.imread('../image/P4_2_cat.jpg', cv2.IMREAD_GRAYSCALE)
print(img2.shape)

# 图像的显示，也可以创建多个窗口
cv2.imshow('image', img2)

# 等待时间，毫秒级，0表示任意键终止
cv2.waitKey(3000)
cv2.destroyAllWindows()

# 保存
cv2.imwrite('./P5_1_mycat.png', img2)

print(type(img2))
print(img2.size)
print(img2.dtype)

# 数据读取-视频
vc = cv2.VideoCapture('../video/P5_1_test.mp4')

# 检查是否打开正确
if vc.isOpened():
    open, frame = vc.read()
else:
    open = False

while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey(10) & 0xFF == 27:
            break
vc.release()
cv2.destroyAllWindows()
