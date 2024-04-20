"""Socket programming in python"""

import socket
import sys

"""
    Notes:
    AF_INET: IPV4
    SCOK_STREAM: Connection Orientated TCP Protocol
    TCP: Transmission Control Protocol
"""

# Try to create a socket
try:
    # Creates a TCP socket connecting to ipv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket successfully created')
except socket.error as err:
    print(f'socket creation failed with error {err}')

port = 80

# Try to get the ip of GitHub
try:
    # Getting the ip of GitHub
    host_ip = socket.gethostbyname('www.github.com') # Output: 140.82.114.3
except socket.gaierror: # gaierror is a error caused by domain tranlation to ip
    print(f'error resolving the host')
    sys.exit()

# Connect to the host using the port
s.connect((host_ip, port))

print(f'Socket has successfully connected to GitHub on port == {host_ip}')