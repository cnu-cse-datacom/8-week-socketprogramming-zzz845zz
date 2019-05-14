import socket
import os


# setting
ip_addr = '10.3.86.51'
port = 9000
blockSize = 2**10
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# open file
fileName = input("Input your file name : ")
f = open(fileName, 'rb')

# get file size
fileSize = os.path.getsize(fileName)

# send file, client information
client_socket.sendto(fileName.encode(), (ip_addr, port))
client_socket.sendto(str(fileSize).encode(), (ip_addr, port))

# send
currentSize=0
try:
    data = f.read(blockSize)
    while data:
        currentSize += client_socket.sendto(data, (ip_addr, port))
        print("currentSize / totalSize = %d/%d, %.6f%%" %(currentSize, fileSize, currentSize/fileSize*100))
        data = f.read(blockSize)
except Exception as e :
    print(e)

print("send complete,", currentSize)