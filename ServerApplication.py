import socket
import threading
import tkinter
import time
import sys

# First, establish an ip address for the server
HOST = '10.141.64.144'

# Make sure the port is identical for the server and all clients
PORT = 8080

# Define the length of the messages to be send and received in bytes
HEADER = 1024

# Character encoding style for encoding and decoding messages that are sent/received
STYLE = "utf-8"

# Indicates whether a single client is connected to the server or not
connected = False

# Create the socket over IPV4 and Transmission Control Protocol (TCP)
    # AF_INET - IPV4
    # SOCK_STREAM - TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

stop_event = threading.Event()

# Socket object used to communicate with a single client
conn = None

def get_input():
    global connected
    time.sleep(1)
    while connected:
        # This will block
        input_message = input("Server: ")
        send_message(input_message)

def send_message(message: str):
    global server, conn
    if conn is not None:
        try:
            # Send a message to the client
            conn.send(message.encode(STYLE))
        except OSError as e:
            print(f"Failed to send: ", {e})

def begin_server():
    global connected, server, conn
    # Tell the socket which ip address and which port it should be associated with
    server.bind((HOST, PORT))
    # Start accepting connections
    server.listen()
    # conn - socket object used to communicate with a single client
    # addr - the client's address
    print("Listening for requests...")
    conn, addr = server.accept()
    with conn:
        print(f"Connection successful by {addr}")
        connected = True
        listen_thread = threading.Thread(target=get_input, daemon=True)
        listen_thread.start()
        while connected:
            # Receive incoming data from client
            data = conn.recv(HEADER)
            if not data:
                break
            # Print out the data received in utf-8 formatting
            message = data.decode(STYLE)
            print(f"Client: {message}")
    print(f"Connection to {addr} lost.")
    connected = False
    stop_event.set()
    server.close()
    sys.exit(1)

def main():
    global connected
    print("Welcome to the Server-Client Application!")
    # Call the function to start the server
    connection_thread = threading.Thread(target=begin_server)
    connection_thread.start()

if __name__ == "__main__":
    main()
