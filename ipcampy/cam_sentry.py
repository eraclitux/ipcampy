'''
File	    : cam_sentry.py
Version	    : 0.0.1
Author	    : Andrea Masi andrea@eraclitux.com 
Description : Move ipcams around and take snapshots
'''
#TODO convert ip_cam to a class to manage many of them
import urllib
import datetime
import time
import os
import requests

CAM_IP   = "192.168.1.150:8001"
DATA_DIR = "/opt/data/ipcam"
USER     = "viewer"
PWD      = "vi3w3r21"

def go_to_position(pos):
	#http://1912.168.1.150:8001/decoder_control.cgi?command=39&user=viewer&pwd=vi3w3r21
	payload = {"user":USER, "pwd":PWD, "command": pos}
	r = requests.get("http://"+CAM_IP+"/decoder_control.cgi", params=payload)
	#print r.url
	#print r.text
	
def main():
	#Wait for cams to complete power cycle
	time.sleep(18)
	#37 is the 4th position
	go_to_position(37)

	date = datetime.datetime.now().strftime("%d%m%Y_%H")
	current_path = DATA_DIR+'/'+date
	try:
		os.mkdir(current_path)
	except OSError:
		print "[ERROR] OSError"

	while 1:
		if datetime.datetime.now().minute == 0:
			date = datetime.datetime.now().strftime("%d%m%Y_%H")
			current_path = DATA_DIR+'/'+date
			try:
				os.mkdir(current_path)
			except OSError:
				print "[ERROR] OSError"
		date = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
		filename = current_path+'/'+date+'.jpg'
		urllib.urlretrieve(
			'http://'+CAM_IP+'/snapshot.cgi?user='+USER+'&pwd='+PWD,
			filename
		)
		os.system('jpegtran -rotate 90 -outfile %s %s' % (filename, filename))
		time.sleep(15)
if __name__ == '__main__':
	main()
