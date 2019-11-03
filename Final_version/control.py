import win32api
import win32con
import os,sys
import time

# 控制
def keyboard_control(dir_tr,limit,begin):


    if dir_tr.find("上") != -1: # 向上 
        win32api.keybd_event(38,0,0,0)
        win32api.keybd_event(38,0,win32con.KEYEVENTF_KEYUP,0)


    elif dir_tr.find("下") != -1: # 向下
        win32api.keybd_event(40,0,0,0)
        win32api.keybd_event(40,0,win32con.KEYEVENTF_KEYUP,0)


    elif dir_tr.find("确认") !=-1: #enter
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)


    elif dir_tr.find("开始") != -1: 
        begin.value=1

    elif dir_tr.find("减速")!=-1 :
        win32api.keybd_event(40,0,0,0)
        time.sleep(0.6)
        win32api.keybd_event(40,0,win32con.KEYEVENTF_KEYUP,0)
    elif dir_tr.find("加速")!=-1 :
        win32api.keybd_event(38,0,0,0)
        time.sleep(0.6)
        win32api.keybd_event(38,0,win32con.KEYEVENTF_KEYUP,0)
        
    elif dir_tr.find("结束")!=-1:
        begin.value=0

    elif dir_tr.find("限速")!=-1:
        number=filter(str.isdigit,dir_tr)
        limit.value=number
        print('limit',limit.value)
