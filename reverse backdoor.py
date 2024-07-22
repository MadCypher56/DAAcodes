import socket

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.0.104",4444))

message = "\n [+] Sent message"
connection.send(message.encode('utf-8'))

recvData = connection.recv(1024)
print(recvData)

connection.close()