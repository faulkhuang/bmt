# encoding: utf-8

import time
import msvcrt
import os
from castro import Castro
from PIL import Image
from PIL import ImageGrab
#import Image

bmt_path = 'D:\\bmt_temp'
record_time = 60
	
def ensure_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)
		print path + "  Create successfully."
	return None

def screenshot(path):
	#print "Input any key to leave program."
	#while True:
	#	time.sleep(1.0)
	os.chdir(path)
	t = time.strftime("%Y_%m_%d") + time.strftime("_%H_%M_%S")
	#Image._initialized = 1
	img = ImageGrab.grab()
	img = img.resize((1920,1080))
	img.save(t+".jpg", "JPEG")
	print "Screenshot !"
	#if msvcrt.kbhit():
	#	break    
	#	print "Bye Bye!"
	return None
	
def record(path,rtime):
	#os.chdir(path)
	t = time.strftime("%Y_%m_%d") + time.strftime("_%H_%M_%S")
	c = Castro(filename = t + ".swf")
	c.init()
	c.start()
	print "Start recording--------"
	time.sleep(rtime)
	c.stop()
	return None

def ensure_castro_path(path):
	print "Setup bmt_temp folder."
	os.environ['CASTRO_DATA_DIR'] = path
	print os.environ['CASTRO_DATA_DIR']
	return None
	
if __name__ == "__main__":
	ensure_castro_path(bmt_path)
	ensure_dir(bmt_path)
	screenshot(bmt_path)
	record(bmt_path, record_time)