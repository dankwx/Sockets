import socket
import json

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# create a object array 'user', each user have a name

user = []

with open('data.json') as json_file:
    myArray = json.load(json_file)

# convert age and weight to string
for i in range(len(myArray)):
    myArray[i]['Age'] = str(myArray[i]['Age'])
    myArray[i]['Weight'] = str(myArray[i]['Weight'])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # send the name, age and weight of each user in myArray, jump line after each user
    for i in range(len(myArray)):
        s.sendall(myArray[i]['Name'].encode())
        s.sendall(myArray[i]['Age'].encode())
        s.sendall(myArray[i]['Weight'].encode())
        s.sendall('  |  '.encode())

    data = s.recv(1024)
    print('Received', repr(data))

    data = s.recv(1024)

print('Received', repr(data))
