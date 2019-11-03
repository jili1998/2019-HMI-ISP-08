import multiprocessing
import time
import os
import image_demo
import video_demo
import number_demo

speed=multiprocessing.Value('i',0)
begin=multiprocessing.Value('i',0)
limit=multiprocessing.Value('i',40)

def image_processing(speed,limit,begin):
    image_demo.processing(speed,limit,begin)


def video_processing(limit,begin):
    video_demo.processing(limit,begin)

def number_processing(speed):
    number_demo.processing(speed,begin)


    
if __name__ == "__main__":
    task1=multiprocessing.Process(target=image_processing,args=(speed,limit,begin,))
    task2=multiprocessing.Process(target=video_processing,args=(limit,begin,))
    task3=multiprocessing.Process(target=number_processing,args=(speed,begin,))
    task1.start()
    task2.start()
    task3.start()





