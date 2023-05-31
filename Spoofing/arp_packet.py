import scapy.all as scapy

if __name__ == '__main__':
	arp = scapy.ARP()

	print(arp.show())
