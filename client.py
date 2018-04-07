from socket import *
import commands
import os
import sys

# Function to print the contents of the server's directory
def ls():

def quit():
	clientSock.close()
	keep_running = False

# Check to see if there is a directory named 'clientDIR' and create one if there isn't
# This will be where we will be storing our files and retreiving them
if not os.path.exists('clientDIR'):
	os.makedirs('clientDIR')

# Change the current directory to our 'clientDIR' directory. By creating it in the
# previous lines, we do not have to navigate many directories to find it
os.chdir('clientDIR')

serverName = 'localhost'
serverPort = 1234
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((serverName, serverPort))

keep_running = True

while keep_running:
	# Prompt for user input	
	user_input = raw_input('>ftp ')

	try:
		command, name = user_input.split(' ')
	except ValueError:	
		command = user_input

	if 'name' in locals():
		if command == 'get':

		if command == 'put':	
	
	if command == 'ls':
	
	if command == 'quit':



"""
	# User chooses to display directory contents
	if user_input == 'ls':
		ls()

	# User chooses to exit
	if user_input == 'quit':
		clientSock.close()
		sys.exit(0)

	#if user_input == 'put':
"""

	data = 'test message from client'
	encoded_data = data.encode()

	bytesSent = int(0)

	clientSock.send(encoded_data)

sys.exit(0)

"""
while bytesSent != len(data):
	bytesSent += clientSock.send(data[bytesSent])
"""
