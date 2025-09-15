import socket
import threading
import tkinter
import time

# First, get the server's ip address, then use an unused port
# Think of the Host as the street address, with the internet being the city
HOST = '10.141.64.144'

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

# Connection for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def get_input():
    global connected
    time.sleep(1)
    while connected:
        # This will block
        input_message = input("Client: ")
        send_message(input_message)

def send_message(message: str):
    global client
    try:
        # Send a message to the server
        client.send(message.encode(STYLE))
    except OSError as e:
        print(f"Failed to send: ", {e})


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
    print("Waiting to connect to server...")
    connection = client.connect((HOST, PORT))
    print(f"Connected to {HOST}")
    connected = True

    # Create and start a separate thread that reads messages from the server
    listening_thread = threading.Thread(target=listen_for_messages)
    listening_thread.start()

    connection_thread = threading.Thread(target=get_input)
    connection_thread.start()

    while connected:
        pass


if __name__ == "__main__":
    main()