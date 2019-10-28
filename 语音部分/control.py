import pymouse,pykeyboard,os,sys
from pymouse import PyMouse
from pykeyboard import PyKeyboard
# 控制
def keyboard_control(dir_tr):
    #ms = PyMouse()
    ks = PyKeyboard()

    if dir_tr.find("上") != -1: # 向上 
        ks.tap_key(ks.up_key)

    elif dir_tr.find("下") != -1: # 向下
        ks.tap_key(ks.down_key)
 
    elif dir_tr.find("左") != -1: # 向左
        ks.tap_key(ks.left_key)
    elif dir_tr.find("右") != -1: # 向右
        ks.tap_key(ks.right_key)
    elif dir_tr.find("开始") != -1: # enter
        ks.tap_key(ks.enter_key)
