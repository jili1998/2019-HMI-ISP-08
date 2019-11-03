import luyin
import wav2pcm
import shibie
import control
import time
import os

i=0
while True:
# 请说出语音指令
    print("\n\n==================================================")
    rec_yuyin = "D:/Python/self_project/luyin/files/test"+str(i)+".wav"
    #print(rec_yuyin)
    luyin.audio_record(rec_yuyin, 3)
    pcm_file = wav2pcm.wav_to_pcm(rec_yuyin)
    asr_result = shibie.shibie(pcm_file) # 识别语音指令
    if len(asr_result) != 0:
        print("Identify Result:", asr_result)
        print("Start Control...")
        control.keyboard_control(asr_result) # 根据识别结果控制键盘
        print("Control End...")
        if asr_result.find("退出") != -1: # 如果是"退出"指令则结束程序
            break;
        time.sleep(1) # 延时1秒
    i=i+1
