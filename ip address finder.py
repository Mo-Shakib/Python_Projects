# this script can find any website IP address
import socket
host = 'www.apple.com' # web address
ip = socket.gethostbyname(host)
print(f'IP of {host} is {ip}')