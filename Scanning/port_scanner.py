import socket
from termcolor import colored

def port_scanner(host):
    opened_ports = []
    closed_ports = 0

    for i in range(1, 65536):
        address = (host, i)

        if sock.connect_ex(address):
            closed_ports += 1
        else:
            opened_ports.append(address[1])

    return opened_ports, closed_ports


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Host: ")
opened_ports, closed_ports = port_scanner(host)

print(colored("{} closed ports".format(closed_ports), "red"))

for i in opened_ports:
    print(colored("Port {} opened".format(i), "green"))

