import time
import config
import os

w1 = "/sys/bus/w1/devices/28-00000494acf0/w1_slave"

def readTemp():
	temp = ""
	raw = open(w1, "r").read()
	f = str((float(raw.split("t=")[-1])/1000)*(9.0/5.0) + 32.0)
	c = str(float(raw.split("t=")[-1])/1000)
	temp += f
	temp += ","
	temp += c
	return temp

class Temperature(object):
	def init(self):
		os.system("echo BB-W1:00A0 > /sys/devices/bone_capemgr.9/slots")	
		
	def read(self):
		init()
		while 1:
			value = readTemp()
			fahrenheit,celcius = value.split(",")
			return fahrenheit +" " + celcius
			time.sleep(2)
