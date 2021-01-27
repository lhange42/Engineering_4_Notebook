#Lukas Hange
from flask import Flask, render_template, request
import RPi.GPIO as GPIO

# basic setup for LED's, gpio pins, flask
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
leds = [22, 23]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, GPIO.LOW)
app = Flask(__name__)

@app.route("/", methods=["GET","POST"]) # 
def index():
	if request.method == 'POST': # asks if the request is a click of one of the button it runs this to determine if it is the on or off
		if request.form.get('btn1') == 'btn1': # requests the data to determine on if it's been prompted on and if so it turns the button on
			GPIO.output(leds, GPIO.HIGH)	
		elif request.form.get('btn2') == 'btn2': # requests the data to determine on if it's been prompted off and if so it turns the button off
			GPIO.output(leds, GPIO.LOW)
		else:
			return render_template("index.html") 
	
	return render_template("index.html")	
     
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80, debug=True)
