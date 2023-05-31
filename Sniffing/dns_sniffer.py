from scapy.all import *

def sniff_dns(packet):
	if packet.haslayer(DNS) and packet.haslayer(IP):
		ip_info = packet[IP]
		dns_info = packet[DNS]

		print(ip_info.src + '---' + dns_info.summary())

if __name__ == '__main__':
	sniff(prn=sniff_dns)
