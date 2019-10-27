import time
from PIL import ImageGrab
import numpy as np
import cv2
import win32api
import win32con


#图像处理部分：
blur_ksize=5  #高斯算子大小
canny_lthreshold=50  #canny算子
canny_hthreshold=150

rho = 1
theta = np.pi / 180
threshold = 15
min_line_length = 40
max_line_gap = 20
 
def roi_mask(img, vertices):
  mask = np.zeros_like(img)
  mask_color = 255
  cv2.fillPoly(mask, vertices, mask_color)
  masked_img = cv2.bitwise_and(img, mask)
  return masked_img
def draw_lines(img, lines, color=[0, 255, 0], thickness=2):
  for line in lines:
    for x1, y1, x2, y2 in line:
      cv2.line(img, (x1, y1), (x2, y2), color, thickness)
 
def hough_lines(img, rho, theta, threshold,
                min_line_len, max_line_gap):
  lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]),
                          minLineLength=min_line_len,
                          maxLineGap=max_line_gap)
  line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
  draw_lines(line_img, lines)
  return line_img








while(1):
              #img = ImageGrab.grab()
#屏幕截取
    im = ImageGrab.grab(bbox=(28,219,660 ,680))
    img1 = np.array(im)
    img=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    #cv2.namedWindow('img',cv2.WINDOW_KEEPRATIO)
    #cv2.resizeWindow('img',646,467)
    #cv2.imshow('img', img)

#图像处理
    #灰度化
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #高斯模糊
    blur_gray=cv2.GaussianBlur(img_gray,(blur_ksize,blur_ksize),0,0)
    #cv2.namedWindow('blur_gray',cv2.WINDOW_KEEPRATIO)
    #cv2.resizeWindow('blur_gray',646,467)
    #cv2.imshow("blur_gray",blur_gray)
    #二值化
    #ret,mask=cv2.threshold(img_gray,190,255,cv2.THRESH_BINARY)
    #canny提取边缘
    edges=cv2.Canny(blur_gray,canny_lthreshold,canny_hthreshold)
    cv2.namedWindow('edges',cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow('edges',646,467)
    cv2.imshow("edges",edges)
    
    #截取区域
    crop_img2=edges[200:250,0:650]
    cv2.imshow("2",crop_img2)

    #霍夫变换
    hough_img=hough_lines(crop_img2,rho,theta,threshold,min_line_length,max_line_gap)
    cv2.imshow('hough',hough_img)


#模拟键盘输入
    #win32api.keybd_event(87,0,0,0)#W
   # win32api.keybd_event(65,0,0,0)#A
   # win32api.keybd_event(68,0,0,0)#S
   # win32api.keybd_event(83,0,0,0)#D
  # win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)#释放按键


    
    k=cv2.waitKey(5)
    if k==ord('q'):
        break
    
  


