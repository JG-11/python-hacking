import socket
from struct import *


def parse_mac_address(mac_address):
	address = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (mac_address[0], mac_address[1], mac_address[2], mac_address[3],\
						mac_address[4], mac_address[5])

	return address


try:
	sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

	while True:
		packet = sock.recvfrom(65535) # https://www.sciencedirect.com/topics/computer-science/registered-port
		packet = packet[0]

		eth_length = 14
		eth_header = packet[:eth_length]

		eth = unpack('!6s6sH', eth_header) # https://docs.python.org/3/library/struct.html#format-strings
		eth_protocol = socket.ntohs(eth[2]) # https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

		dest_mac = parse_mac_address(packet[0:6])
		src_mac = parse_mac_address(packet[6:12])

		print(f'Destination MAC {dest_mac} - Source MAC {src_mac} - Protocol Number {eth_protocol}')

except KeyboardInterrupt:
	print('Program Finished')
