import threading
import socket

alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break


def client_send():
    print("Type your message and press Enter to send. Type 'quit' to exit.")
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


recieve_thread = threading.Thread(target = client_receive)
recieve_thread.start()