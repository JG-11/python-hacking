import argparse
import socket
from termcolor import colored
from threading import Thread

def scan_address(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if sock.connect_ex((host, port)):
        print(colored('{}/tcp closed'.format(port), 'red'))
    else:
        print(colored('{}/tcp opened'.format(port), 'green'))


def scan_host(host, ports):
    for port in ports:
        thread = Thread(target=scan_address, args=(host, int(port)))
        thread.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Port scanner')
    parser.add_argument('--host', help='Host IPv4 address')
    parser.add_argument('--port', help='Ports separated by comma')

    args = parser.parse_args()
    scan_host(args.host, args.port.split(','))
