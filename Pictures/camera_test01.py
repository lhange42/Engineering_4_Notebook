import time
import picamera
#imageNum = 0
def file():
	#imageNum = imageNum + 1
	#fileName = "camera_test" + str(imageNum) + ".jpg"	
	return(fileName)

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	# Camera warm-up time
	print("running")
	time.sleep(2)
	camera.capture('camera_test.jpg')
	print("done")
