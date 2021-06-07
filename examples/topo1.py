#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5bc Demo")
    
    epd = epd7in5bc.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)

    # Drawing on the image
    logging.info("Drawing")    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    

    
    logging.info("4.read bmp file on window")
    blackimage1 = Image.new('1', (epd.width, epd.height), 255)  # 298*126
    redimage1 = Image.new('1', (epd.width, epd.height), 255)  # 298*126    
    newimage = Image.open(os.path.join(picdir, 'topo_4.bmp'))
    blackimage1.paste(newimage, (50,10))    
    epd.display(epd.getbuffer(blackimage1), epd.getbuffer(redimage1))
    
    # logging.info("Clear...")
    # epd.init()
    # epd.Clear()
    
    # logging.info("Goto Sleep...")
    # epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5bc.epdconfig.module_exit()
    exit()
