import socket

target_host = "localhost"
target_port = 21

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
client.connect((target_host, target_port))

#send some data
client.send(b"sometext123")

#recive some data
response = client.recv(4096)

print(response.decode())
client.close()
