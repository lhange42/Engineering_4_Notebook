#Headless
#Lukas Hange

import time
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
accelerometer = Adafruit_LSM303.LSM303()

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0) 
font = ImageFont.load_default()

disp.image(image)
disp.display() 

radius = 5

while True:
	draw.rectangle`((0, 0, width, height), outline=0, fill=0)
	accel, mag = accelerometer.read() 
	accel_y, accel_x, accel_z = accel# I switched x and y because the way my OLED is orientated in relation to the acceleramtor these would be opposite.
	mag_x, mag_y, mag_z = mag
	draw.ellipse((
