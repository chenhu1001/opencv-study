# 1)使用高斯滤波器，以平滑图像，滤除噪声。
# 2)计算图像中每个像素点的梯度强度和方向。
# 3)应用非极大值 (Non-Maximum Suppression) 抑制，以消除边缘检测带来的杂散响应。
# 4)应用双阈值 (Double-Threshold) 检测来确定真实的和潜在的边缘。
# 5)通过抑制孤立的弱边缘最终完成边缘检测。