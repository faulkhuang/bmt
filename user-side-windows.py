# encoding: utf-8

import time
from PIL import Image
from PIL import ImageGrab

while True:
    time.sleep(1.0)
    t = time.strftime("%Y_%m_%d") + time.strftime("_%H_%M_%S")
    img = ImageGrab.grab()
    img = img.resize((1920,1080))
    img.save(t+".jpg","JPEG")
