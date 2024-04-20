import socket

s = socket.socket()
print('Socket created')
port = 56789

# bind takes a ip and port
s.bind(('', port)) # the ip is empty as to listent for other computers on the network
print(f'socket binded to port{port}')

# The limit of connections our server will listen to be refusal
s.listen(5)
print('socket is listening')

while True:
    # Accept connection from a socket s
    c, addr = s.accept() # c: ip, addr: port

    print('Got connection from', addr)
    message = ("Thank you for connecting")
    
    # Send a thank you message to client for connecting. Message must be in bytes hence encode
    c.send(message.encode())
    
    # Close connection
    c.close()