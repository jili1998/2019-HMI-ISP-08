import time
from PIL import ImageGrab
import numpy as np
import cv2
import win32api
import win32con
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
    
  


