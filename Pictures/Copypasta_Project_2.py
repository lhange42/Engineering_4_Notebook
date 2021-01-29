import time
import picamera
frame = 1

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	while True:
		i = str(input("Click enter to take a frame or x then enter to exit: "))
		try:
			if i == "":
				camera.capture('/home/pi/Documents/Engineering_4_Notebook/Pictures/animation/frame%03d.jpg' % frame)
				frame += 1
			elif i == "x":
				camera.stop_preview()
				break
		except KeyboardInterrupt:
			camera.stop_preview()
			break
