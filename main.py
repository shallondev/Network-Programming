"""Socket programming in python"""

import socket
import sys

"""
    Notes:
    AF_INET: IPV4
    SCOK_STREAM: Connection Orientated TCP Protocol
    TCP: Transmission Control Protocol
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)