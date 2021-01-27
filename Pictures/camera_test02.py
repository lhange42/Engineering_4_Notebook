#Camera Test 2 - For Effects



import time
import picamera
imageNum = 0
def file():
	imageNum = imageNum + 1
	fileName = "camera_test" + str(imageNum) + ".jpg"	
	return(fileName)

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2)

	for i in range(5):
		time.sleep(2)

		#for every iteration, change the effect
		if i == 0:
			camera.image_effect = 'colorswap'
		elif i == 1:
			camera.image_effect = 'sketch'
		elif i == 2:
			camera.image_effect = 'cartoon'
		elif i == 3:
			camera.image_effect = 'washedout'
		elif i == 4:
			camera.image_effect = 'film'
		else:
			camera.image_effect = 'none'
		
		#capture the photo
		time.sleep(1)
		camera.capture('camera_test.jpg')
		time.sleep(2)

		#tell what number loop we are on
		print("loop : " + i) 
	
	#when program is completed
	camera.stop_preview()
	print("done")
