message = "\n [+] Sent message"
connect.send(message.encode('utf-8'))

recvData = connect.recv(1024)
print(recvData)

connect.close()