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
padding = 5
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0) 
font = ImageFont.load_default()

disp.image(image)
disp.display() 
timeVar = 0
radius = 5

while True:
	if timeVar > width:
		draw.rectangle((0, 0, width, height), outline=0, fill=0)
		timeVar = 0
		

	if timeVar == 0:
		draw.rectangle((0+padding, height-padding, width+padding, -height-padding), outline=255, fill=0)
		print("resets t")
		
	acc, mag = accelerometer.read() 
	acc_x, acc_y, acc_z = acc # this gives me all my acceleration data even though I only need x acceleration I have to store all of them.
	mag_x, mag_y, mag_z = mag
	xAcc = abs(acc_x*.1) + padding # sets up the x acceleration data into data values for graphing
	
	draw.ellipse((timeVar,height-xAcc,50,50), outline = 255, fill = 255)# will draw a dot at each point and the points will be charted on the graph 
	print(xAcc)
	time.sleep(.5)
	timeVar = timeVar + 1
	
	disp.image(image)
	disp.display()
