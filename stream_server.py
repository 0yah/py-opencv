
import socket
import time
import cv2
import numpy
 
def ReceiveVideo():
	address = ('', 8002)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(address)
	s.listen(1)
 
	# Read all bytes
	def recvall(sock, count):
		buf = b''
		while count:
			newbuf = sock.recv(count)
			if not newbuf: return None
			buf += newbuf
			count -= len(newbuf)
		return buf
		
	# Accept TCP connection and returns (conn, address), where conn is a new socket object, can be used to receive and transmit data. addr is the address of the connecting client.
	# Wait for a connection is not connected
	conn, addr = s.accept()
	print('New connection from:'+str(addr))
	while True:
		start = time.time()#For frame rate calculation
		length = recvall(conn,16)#Get the file length
		stringData = recvall(conn, int(length))# according to documents obtained length, to obtain image files
		data = numpy.frombuffer(stringData, numpy.uint8)# the acquired data into the character stream 1-dimensional array
		decimg=cv2.imdecode(data,cv2.IMREAD_COLOR) # decoded into an image array
		#Show the image 
		cv2.imshow('SERVER',decimg)
 
        # Frame rate information return, the main purpose is to test two-way communication can
		end = time.time()
		seconds = end - start
		fps  = 1/seconds;
		conn.send(bytes(str(int(fps)),encoding='utf-8'))
		k = cv2.waitKey(10)&0xff
		if k == 27:
			break
	s.close()
	cv2.destroyAllWindows()
 
if __name__ == '__main__':
	ReceiveVideo()