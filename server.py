# Server code written based off of Assignment 1 handout
# and some help from stackoverflow.com and python.org documentation

from socket import *
import commands
import sys
import os

#TODO
def ls():
	commands.getstatusoutput('ls -l > toSend.txt')
	print("Ready to send info to client")
	
	fileObject = open("toSend.txt", "r")
	
	fileSocket = socket.socket(socker.AF_INET, socket.SOCK_STREAM)
	

#TODO
def quit():
	connectionSocket.close()

#TODO
def put(filename):

#TODO
def get(filename):

# Check to see if there is a directory named 'Test' and create one if there isn't
# This will be where we will be storing our files and retreiving them
if not os.path.exists('test'):
	os.makedirs('test')

# Change the current directory to our 'Test' directory. By creating it in the
# previous lines, we do not have to navigate many directories to find it
os.chdir('test')

# The port we want to listen to
serverPort = 1234

# Creating a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)	

# Binding the socket to the port
serverSocket.bind(('localhost', serverPort))

# Start listening and limit the number of connections to 1
serverSocket.listen(1)

print("The server is ready to receive")

while 1:
	connectionSocket, addr = serverSocket.accept()
	
	received_data = connectionSocket.recv(1024)
	received_data.decode()

	try:
		command, name = received_data.split(' ')
	except ValueError:
		command = received_data

	if command == 'ls':
		ls()

	else if command == 'quit()':
		quit()
		break

	else:
		if command == 'put':
			put(name)

		if command == 'get':
			get(name)

connectionSocket.close()

'''
connectionSocket, addr = serverSocket.accept()
data =  connectionSocket.recv(255)
data.decode()
print(data)

connectionSocket.close()
'''
