import time
from PIL import ImageGrab
import numpy as np
import cv2
import win32api
import win32con
import operator


def processing(speed,begin):
    while(begin.value==0):
        if begin.value==1:
            break
    while(1):
        i=0
        number1=number2=0
        im = ImageGrab.grab(bbox=(0,50,800 ,640))
        img1 = np.array(im)
        img=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        crop_img2=img[530:563,665:685]
        #cv2.imshow("2",crop_img2)

        crop_img3=img[530:563,685:705]
        #cv2.imshow("3",crop_img3)


        #img=cv2.imread("D:\Python\self_project\picture\\"+i+".ipg")
        for i in range(9):
            img=cv2.imread("D:/Python/self_project/picture/"+i+".ipg")
            img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1",img)

            ret,thresh=cv2.threshold(img,130,255,0)
            ret,thresh2=cv2.threshold(crop_img2,130,255,0)
            ret,thresh3=cv2.threshold(crop_img3,130,255,0)

            contours1,hierarchy=cv2.findContours(thresh,2,1)
            cnt1=contours1[0]

            contours2,hierarchy=cv2.findContours(thresh2,2,1)
            cnt2=contours2[0]

            contours3,hierarchy=cv2.findContours(thresh3,2,1)
            cnt3=contours3[0]
            match1=cv2.matchShapes(cnt1,cnt2,1,0.0)
            match2=cv2.matchShape(cnt1,cnt3,1,0.0)
            if match1<0.06:
                number1=i
            if match2<0.06:
                number2=i


        speed.value=number1*10+number2
        
        k=cv2.waitKey(5)
        if k==ord('q') or begin.value==0:
            break
