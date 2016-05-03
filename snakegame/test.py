import os, sys, time
import thread

stop = ""
def get_dev_input(threadName, delay):
	dev = os.open("../../../dev/rfcomm0", os.O_RDONLY)
	while True:
		#stat = dev.tell()
		global stop 
		stop = os.read(dev,1)
		print stop 
	#size = os.lseek(dev ,0,os.SEEK_SET)
	#if os.read(dev, 1) == "":
	#	print "Empty"
	#print size
	#while os.stat("../../../dev/rfcomm0").st_size == 0:
	#time.sleep(1)
		#print "Empty"
	
	#print "full"
	#os.close(dev)

try:
	thread.start_new_thread(get_dev_input, ("Thread-1", 4))
except:
	print "unable to create thread"
while True:
	time.sleep(1)
	print "testing"
	if stop == 'w':
		print "stopping!"
		break