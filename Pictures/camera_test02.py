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
			camera.capture('camera_test_colorswap.jpg')
		elif i == 1:
			camera.image_effect = 'sketch'
			camera.capture('camera_test_sketch.jpg')
		elif i == 2:
			camera.image_effect = 'cartoon'
			camera.capture('camera_test_cartoon.jpg')
		elif i == 3:
			camera.image_effect = 'washedout'
			camera.capture('camera_test_washedout.jpg')
		elif i == 4:
			camera.image_effect = 'film'
			camera.capture('camera_test_none.jpg')
		else:
			camera.image_effect = 'none'
			camera.capture('camera_test_film.jpg')
		
		#capture the photo
		time.sleep(2)

		#tell what number loop we are on
		print("loop : " + str(i)) 
	
	#when program is completed
	camera.stop_preview()
	print("done")
