import time
from PIL import ImageGrab
import numpy as np
import cv2
import win32api
import win32con
import operator
import time

def processing(speed,begin):
    while(begin.value==0):
        if begin.value==1:
            break
    path_temp="D:/Python/self_project/picture/n0.png"
    img_temp=cv2.imread(path_temp)
    img_temp=cv2.cvtColor(img_temp,cv2.COLOR_BGR2GRAY)
    ret,thresh0=cv2.threshold(img_temp,130,255,0)        
    contours0,hierarchy=cv2.findContours(thresh0,2,1)
    cnt0=contours0[0]   
    while(1):
        temp1=temp2=5
        i=0
        number1=number2=0
        im = ImageGrab.grab(bbox=(0,50,800 ,640))
        img1 = np.array(im)
        img=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        crop_img2=img[534:557,670:687]
        #cv2.imshow("2",crop_img2)

        crop_img3=img[534:557,687:704]
        #cv2.imshow("3",crop_img3)
        
        ret,thresh2=cv2.threshold(crop_img2,130,255,0)
        ret,thresh3=cv2.threshold(crop_img3,130,255,0)
            
        contours2,hierarchy=cv2.findContours(thresh2,2,1)
        if contours2 :
            cnt2=contours2[0]
        else :
            cnt2=cnt0
        contours3,hierarchy=cv2.findContours(thresh3,2,1)
        cnt3=contours3[0]

        for i in range(10):
            path="D:/Python/self_project/picture/n"+str(i)+".png"
            img_num=cv2.imread(path)
            img_num=cv2.cvtColor(img_num,cv2.COLOR_BGR2GRAY)

            ret,thresh=cv2.threshold(img_num,130,255,0)
            
            contours1,hierarchy=cv2.findContours(thresh,2,1)
            cnt1=contours1[0]
            match1=cv2.matchShapes(cnt1,cnt2,1,0.0)
            match2=cv2.matchShapes(cnt1,cnt3,1,0.0)
            if match1<temp1:
                temp1=match1
                number1=i
            if match2<temp2:
                temp2=match2
                number2=i
        
        speed.value=number1*10+number2
        if speed.value>=80:
            speed.value=number2
        #print('speeddddddddddddddddd:',speed.value)
        k=cv2.waitKey(5)
        if k==ord('q') or begin.value==0:
            break

