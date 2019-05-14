import socket

# setting
blockSize = 2 ** 10
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 9000))

# receive and print file information
fileName, addr = server_socket.recvfrom(blockSize)
fileSize, _ = server_socket.recvfrom(blockSize)
fileSize = int(fileSize)
print("file recv start from", addr)
print(fileName)
print("File Name : %s" %fileName.decode())
print("File Size : %d" % fileSize)

# open file
print("written File Name : receive")
receiveFile = open("receive", 'wb')

# receive
currentSize = 0
receiveData = bytes()
try:
    data, _ = server_socket.recvfrom(blockSize)
    while data:
        receiveData += data
        currentSize += len(data)
        print("currentSize / totalSize = %d/%d, %.6f%%" %(currentSize, fileSize, currentSize/fileSize*100))

        if currentSize>=fileSize:
            break

        data, a= server_socket.recvfrom(blockSize)

except Exception as e:
    print(e)

# write and close
print("receive success")
receiveFile.write(receiveData)
receiveFile.close()