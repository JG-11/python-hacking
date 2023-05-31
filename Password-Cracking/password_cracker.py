import hashlib
import urllib.request
from termcolor import colored

PASSWORDS_LIST = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt'

def crack_password(password, hashing):
	with urllib.request.urlopen(PASSWORDS_LIST) as response:
		for option in response.read().decode().split('\n'):
			if hashing == 0:
				hash = hashlib.md5()
			elif hashing == 1:
				hash = hashlib.sha1()
			elif hashing == 2:
				hash = hashlib.sha256()
			elif hashing == 3:
				hash = hashlib.sha512()

			hash.update(option.encode())
			if hash.hexdigest() == password:
				return option
	return None


if __name__ == '__main__':
	password = input('Type password to crack: ')
	hashing = int(input('[0] md5\n[1] sha1\n[2] sha256\n[3] sha512\nEnter hashing method: '))

	if hashing < 0 or hashing > 3:
		print('Invalid hashing method')
		print('Finishing program')

		exit()

	ans = crack_password(password, hashing)
	if ans:
		print(colored('Password found: ' + ans, 'green'))
	else:
		print(colored('Password not found', 'red'))
