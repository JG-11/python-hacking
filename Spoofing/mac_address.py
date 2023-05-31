import scapy.all as scapy

BROADCAST = "ff:ff:ff:ff:ff:ff"

def get_mac_address(ip):
	arp = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst=BROADCAST)
	request = broadcast / arp
	answer = scapy.srp(request, timeout=1, verbose=False)[0]

	if len(answer) == 0:
		return None, None

	return answer[0][1].psrc, answer[0][1].hwsrc


if __name__ == '__main__':
	destination_ip = "1.1.1.1"

	response_ip, response_mac = get_mac_address(destination_ip)

	if response_ip == None and response_mac == None:
		print('Impossible to get MAC address from ' + destination_ip)
	else:
		print('MAC address of ' + response_ip + " = " + response_mac)
