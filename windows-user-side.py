# encoding: utf-8

import time
import msvcrt
import os
from castro import Castro
from PIL import Image
from PIL import ImageGrab

bmt_path = 'D:\\30_Python'

def ensure_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)
	return

def screenshot():
	#print "Input any key to leave program."
	#while True:
	#	time.sleep(1.0)
	os.chdir('D:\\30_Python')
	t = time.strftime("%Y_%m_%d") + time.strftime("_%H_%M_%S")
	img = ImageGrab.grab()
	img = img.resize((1920,1080))
	img.save(t+".jpg","JPEG")
	#if msvcrt.kbhit():
	#	break    
	#	print "Bye Bye!"
	return
	
def record(rtime):
	os.chdir('D:\\30_Python')
	t = time.strftime("%Y_%m_%d") + time.strftime("_%H_%M_%S")
	c = Castro(filename = t + ".swf")
	c.start()
	time.sleep(rtime)
	c.stop()
	
if __name__ == "__main__":
	ensure_dir(bmt_path)
	#screenshot()
	record(60)