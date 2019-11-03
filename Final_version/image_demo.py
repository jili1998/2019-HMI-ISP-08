import time
from PIL import ImageGrab
import numpy as np
import cv2
import win32api
import win32con



#图像处理部分：

def abs_sobel_thresh(img, orient='x', thresh_min=30, thresh_max=130):
    #装换为灰度图片
    gray = img
    #使用cv2.Sobel()计算计算x方向或y方向的导数
    abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 1, 0))

    #阈值过滤
    scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
    binary_output = np.zeros_like(scaled_sobel)
    binary_output[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 255

    return binary_output

def get_M_Minv():
    src = np.float32([[(0, 500), (300, 0), (490, 0), (790, 500)]])
    dst = np.float32([[(100,500), (100, 0), (690, 0), (690, 500)]])
    #dst = np.float32([[(220, 690), (180, 0), (710, 0), (570, 690)]])

    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst,src)
    return M,Minv



def processing(speed,limit,begin):
    while(begin.value==0):
        if begin.value==1:
            break
    time.sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    cv2.namedWindow('mask',cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow('mask',646,467)
    blur_ksize=5  #高斯算子大小
    canny_lthreshold=20  #canny算子
    canny_hthreshold=80

    cycle_number=0
    times=18
    
    while(1):
                  #img = ImageGrab.grab()
    #屏幕截取
        im = ImageGrab.grab(bbox=(0,50,800 ,640))
        img1 = np.array(im)
        img=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

    #图像处理
        #灰度化
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #高斯模糊
        blur_gray=cv2.GaussianBlur(img_gray,(blur_ksize,blur_ksize),0,0)
          
        #二值化
        #ret,mask=cv2.threshold(blur_gray,104,255,cv2.THRESH_BINARY)
        mask=cv2.adaptiveThreshold(blur_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,5,3)
        #mask=abs_sobel_thresh(blur_gray)

        #cv2.imshow("mask",mask)
        
        #截取区域
        #crop_img2=mask[280:370,5:795]
        crop_img2=mask[270:370,5:795]
        #cv2.imshow("2",crop_img2)
        crop_img=cv2.resize(crop_img2,(790,600),cv2.INTER_AREA)



    #矩阵变换
        #thresholded_wraped = cv2.warpPerspective(crop_img, get_M_Minv()[0], crop_img.shape[1::-1], flags=cv2.INTER_LINEAR)
        #cv2.imshow('M',thresholded_wraped)



    #键盘操作
    #释放键盘
        win32api.keybd_event(38,0,win32con.KEYEVENTF_KEYUP,0)


        cycle_number+=1
        if speed.value>=limit.value:
            win32api.keybd_event(40,0,0,0)
            time.sleep(0.5)
            win32api.keybd_event(40,0,win32con.KEYEVENTF_KEYUP,0)
        if cycle_number==times:
            cycle_number=0
            win32api.keybd_event(38,0,0,0)
            
        i=0
        j=0
        area_left=0
        area_right=0
        #count_left=0
        #count_right=0

        for j in range(crop_img2.shape[0]-1):
            for i in range(int(crop_img2.shape[1]/2)-2):
                if crop_img2[j,i]==255:
                    area_left+=1
                    #count_left+=1
                if crop_img2[j,i+int(crop_img2.shape[1]/2)]==255:
                    area_right+=1
                    #count_right+=1
           # cha=count_left-count_right
            
            #cv2.circle(img,(int(crop_img2.shape[1]/2)+cha,j+270,),1,(0,255,0),3)
            #count_left=count_right=0
        win32api.keybd_event(37,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(39,0,win32con.KEYEVENTF_KEYUP,0)
        if area_left-area_right>1000:
            win32api.keybd_event(39,0,0,0)

        elif area_right-area_left>1000:
            win32api.keybd_event(37,0,0,0)
        cv2.line(img,(400,0),(400,590),[255,0,0],2)
        cv2.imshow("2",img)




        k=cv2.waitKey(5)
        if k==ord('q') or begin.value==0:
            win32api.keybd_event(38,0,win32con.KEYEVENTF_KEYUP,0)
            win32api.keybd_event(37,0,win32con.KEYEVENTF_KEYUP,0)
            win32api.keybd_event(39,0,win32con.KEYEVENTF_KEYUP,0)

            break
    
  


