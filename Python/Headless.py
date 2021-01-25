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
width = disp.width# makes the variable width equal to the width of the screen
height = disp.height# makes the height variable equal to the screen height
padding = 5
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)#draws a black rectangle that basically resets the screen 
font = ImageFont.load_default()

disp.image(image)
disp.display() 
timeVar = padding # sets up the time variable that starts at the y-axis which is padding


while True:
	if timeVar > width: #if the time variable which is the x coordinate of each point goes of the screen it resets the screen and variable
		draw.rectangle((0, 0, width, height), outline=0, fill=0)
		timeVar = padding
		draw.rectangle((0+padding, height-padding, width+padding, -height-padding), outline=255, fill=0)
		print("resets t")
		
	acc, mag = accelerometer.read() 
	acc_x, acc_y, acc_z = acc # this gives me all my acceleration data even though I only need x acceleration I have to store all of them.
	mag_x, mag_y, mag_z = mag
	xAcc = abs((acc_x*.025)*1.5) + padding # This sets up my data into more appealing data since when the accelerometer is at rest it returns a range of 17 to 22 roughly and this makes those be at zero why also trying to create a more identifiable difference in acceleration

	if xAcc < 5: # If acceleration drops below 5 then return it to 5 just so its visible that points are being created
		xAcc = 5

	draw.ellipse((timeVar,height-xAcc,timeVar+1,height-xAcc+1), outline = 255, fill = 255)# will draw a dot at each point and the points will be charted on the graph 

	print(xAcc)

	timeVar = timeVar + 1 # increases the timeVar by 1 every run through of the while
	
	time.sleep(1)
	
	disp.image(image) 
	disp.display()#displays the change
