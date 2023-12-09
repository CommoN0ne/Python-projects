import socket
import threading

bind_ip = "192.168.1.28"
bind_port = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip ,bind_port))
    server.listen(5)
    print(f'[*] Listening on {bind_ip}:{bind_port}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        # b' for byte object
        sock.send(b'ACKKK')

if __name__ == '__main__':
    main()
