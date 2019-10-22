import os

def wav_to_pcm(wav_file):
    pcm_file = "%s.pcm" %(wav_file.split(".")[0])

    os.system("ffmpeg -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s"%(wav_file,pcm_file))

    return pcm_file
#将WAV格式文件转换为更适合百度Api所使用的pcm格式
