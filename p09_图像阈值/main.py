import cv2  # 导入OpenCV库，用于图像处理
import matplotlib.pyplot as plt  # 导入Matplotlib库，用于图像显示

# 读取图像文件
img = cv2.imread('../image/P5_1_mycat.png')

# 对图像进行阈值处理，使用不同的阈值类型
# 固定阈值二值化处理
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 反向二值化处理
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 截断阈值处理
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# 阈值为零处理
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# 反向阈值为零处理
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# 定义标题列表
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# 定义图像列表
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# 使用Matplotlib显示图像
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')  # 在2行3列的子图中显示图像
    plt.title(titles[i])  # 设置子图标题
    plt.xticks([]), plt.yticks([])  # 去掉x轴和y轴刻度
plt.show()  # 显示所有子图
