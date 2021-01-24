
import socket
import cv2
import sys
import numpy
import time
 
def SendVideo():

	address = ('127.0.0.1', 8002)
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect(address)
	except socket.error as msg:
		print(msg)
		sys.exit(1)
 
	# Get image feed from the webcam
	capture = cv2.VideoCapture(0)
	# Reads an image, the reading is successful: ret = 1 frame = frame image to read; reading failure: ret = 0
	ret, frame = capture.read()
	# Compression parameter, followed cv2.imencode will be used for jpeg, the 15 representative image quality, the higher the better the image quality on behalf of 0-100, default 95
	encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),15]
 
    
	while ret:#While ret == 1:

		# 0.1S to stop sending prevent excessive services to handle, however, if a lot of server-side processing, you should increase this value
		time.sleep(0.01)
		# Cv2.imencode image stream data format conversion (encoding) into, assigned to the memory cache; mainly for compressing image data format, to facilitate the transmission network
		# '. Jpg' represents a picture in accordance with the jpg format encoding.
		result, imgencode = cv2.imencode('.jpg', frame, encode_param)
		# Create a matrix
		data = numpy.array(imgencode)
		# Numpy converted into matrix form characters for transmission over the network
		stringData = data.tostring()
		
		#Length transmission data to be transmitted
		#ljust () method returns a string of the original left-aligned and padded with spaces to the specified length of the new string
		sock.send(str.encode(str(len(stringData)).ljust(16)));
		#send data
		sock.send(stringData)
		 # Read value returned by the server
		receive = sock.recv(1024)
		if len(receive):print(str(receive,encoding='utf-8'))
		#Read the next frame pictures

		ret, frame = capture.read()
		if cv2.waitKey(10) == 27:
			break
	sock.close()
	
if __name__ == '__main__':
	SendVideo()
 

