import time
from PIL import ImageGrab
import numpy as np
import cv2
import win32api
import win32con

#图像处理部分：
blur_ksize = 5  # Gaussian blur kernel size
canny_lthreshold = 50  # Canny edge detection low threshold
canny_hthreshold = 150  # Canny edge detection high threshold

# Hough transform parameters
rho = 1#rho的步长，即直线到图像原点(0,0)点的距离
theta = np.pi / 180#theta的范围
threshold = 15#累加器中的值高于它时才认为是一条直线
min_line_length = 40#线的最短长度，比这个短的都被忽略
max_line_gap = 20#两条直线之间的最大间隔，小于此值，认为是一条直线

def roi_mask(img, vertices):
  mask = np.zeros_like(img)
 
  if len(img.shape) > 2:
    channel_count = img.shape[2] 
    mask_color = (255,) * channel_count
  else:
    mask_color = 255
  cv2.fillPoly(mask, vertices, mask_color)
  masked_img = cv2.bitwise_and(img, mask)#img&mask，经过此操作后，兴趣区域以外的部分被蒙住了，只留下兴趣区域的图像
  return masked_img

def draw_roi(img, vertices):
  cv2.polylines(img, vertices, True, [255, 0, 0], thickness=2)

def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
  for line in lines:
    for x1, y1, x2, y2 in line:
      cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
  lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)#函数输出的直接就是一组直线点的坐标位置（每条直线用两个点表示[x1,y1],[x2,y2]）
  line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)#生成绘制直线的绘图板，黑底
  # draw_lines(line_img, lines)
  draw_lanes(line_img, lines)
  return line_img



def process_an_image(img):
  roi_vtx = np.array([[(0, img.shape[0]), (460, 325), (520, 325), (img.shape[1], img.shape[0])]])#目标区域的四个点坐标，roi_vtx是一个三维的数组
  gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)#图像转换为灰度图
  blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)#使用高斯模糊去噪声
  edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)#使用Canny进行边缘检测
  roi_edges = roi_mask(edges, roi_vtx)#对边缘检测的图像生成图像蒙板，去掉不感兴趣的区域，保留兴趣区
  line_img = hough_lines(roi_edges, rho, theta, threshold, min_line_length, max_line_gap)#使用霍夫直线检测，并且绘制直线
  res_img = cv2.addWeighted(img, 0.8, line_img, 1, 0)#将处理后的图像与原图做融合
  return res_img



while(1):
              #img = ImageGrab.grab()
#屏幕截取
    img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
    im = np.array(img)
    cv2.imshow('cv image', im)

#图像处理





#模拟键盘输入
    win32api.keybd_event(87,0,0,0)#W
    win32api.keybd_event(65,0,0,0)#A
    win32api.keybd_event(68,0,0,0)#S
    win32api.keybd_event(83,0,0,0)#D
    win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)#释放按键


    
    k=cv2.waitKey(5)
    if k==ord('q'):
        break
    
  


