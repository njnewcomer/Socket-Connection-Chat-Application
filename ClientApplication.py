import socket
import threading
import tkinter

# First, get the server's ip address, then use an unused port
# Think of the Host as the street address, with the internet being the city
HOST = '10.141.215.186'

# Specifies the endpoint where communication occurs
# Think of the Port as the house number
PORT = 8080

# Define the size of the header (the length of the message in bytes)
# Think of the Header as the amount of mail the mailman can give you
HEADER = 1024

# Character encoding style for encoding and decoding messages that are sent/received
STYLE = "utf-8"

# Indicates whether a single client is connected to the server or not
connected = False


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # Attempt to establish connection with the server
    connection = client.connect((HOST, PORT))
    print(f"Connection successful at ", {connection})
    # Send a message to the server
    message = "S"
    client.send(message.encode(STYLE))
    # Receive data from the server
    data = client.recv(HEADER)
    # Print out the data received in utf-8 formatting
    message = data.decode(STYLE )
    print(f"Server: {message}")"""

def send_message(message: str):
    global client
    # Send a message to the server
    client.send(message.encode(STYLE))
    # Receive data from the server
    data = client.recv(HEADER)
    # Print out the data received in utf-8 formatting
    message = data.decode(STYLE)
    print(f"Server: {message}") 

def listen_for_messages():
    global connected
    while connected:
        data = client.recv(HEADER)
        message = data.decode(STYLE)
        print(f"Server: {message}")


def main():
    global client, HOST, PORT, connected
    print("Welcome to the Server-Client Chat Application!\n")

    # Attempt to establish connection with the server
    connection = client.connect((HOST, PORT))
    connected = True

    # message = "S"
    # send_message(message)

    listening_thread = threading.Thread(target=listen_for_messages)
    listening_thread.start()

if __name__ == "__main__":
    main()

