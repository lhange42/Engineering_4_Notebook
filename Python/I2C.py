import time
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
accelerometer = Adafruit_LSM303.LSM303() # accelerometer setup
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) # dislay setup
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image) # gets drwaing object to draw on image
draw.rectangle((0,0,width,height), outline=0, fill=0) # clears screen

# variables to help drawing
padding = 2
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default()

while True:
	acc, mag = accelerometer.read() # gets accelerometer data
	acc_x, acc_y, acc_z = acc
	mag_x, mag_y, mag_z = mag
	
	draw.text((x, top), "Accelerometer Data:", font=font, fill=255) # displays text of " acceleramtor data"
	draw.text((x, top + 10), "Acc x ={0}".format(round(acc_x / 100, 3)), font=font, fill=255) # displays the x value acceleration and rounds it to 3 
	draw.text((x, top + 20), "Acc y ={0}".format(round(acc_y / 100, 3)), font=font, fill=255) # displays the y value acceleration and rounds it to 3
	draw.text((x, top + 30), "Acc z ={0}".format(round(acc_z / 100, 3)), font=font, fill=255) # displays the z value acceleration and rounds it to 3

	disp.image(image)
	disp.display()
	
	draw.rectangle((100, 12, 55, 50), outline=0, fill=0)
	disp.image(image)
	disp.display()
