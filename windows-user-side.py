# encoding: utf-8

import time
import msvcrt
import os
#from castro import Castro
from PIL import Image
from PIL import ImageGrab

def ensure_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)
		print path + "  Create successfully."

def screenshot(path):
	#print "Input any key to leave program."
	#while True:
	#	time.sleep(1.0)
	os.chdir(path)
	t = time.strftime("%Y_%m_%d") + time.strftime("_%H_%M_%S")
	img = ImageGrab.grab()
	img = img.resize((1920,1080))
	img.save(t+".jpg","JPEG")
	#if msvcrt.kbhit():
	#	break    
	#	print "Bye Bye!"
	
def record(path,rtime):
	#os.chdir(path)
	t = time.strftime("%Y_%m_%d") + time.strftime("_%H_%M_%S")
	c = Castro(filename = t + ".swf")
	c.start()
	time.sleep(rtime)
	c.stop()

def ensure_castro_path(path):
	os.environ['CASTRO_DATA_DIR'] = path
	print os.environ['CASTRO_DATA_DIR']
	
if __name__ == "__main__":
	bmt_path = 'D:\\bmt_temp'
	record_time = 60
	ensure_castro_path(bmt_path)
	#ensure_dir(bmt_path)
	#screenshot(bmt_path)
	#record(bmt_path, record_time)