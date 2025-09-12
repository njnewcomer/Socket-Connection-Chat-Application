import socket
import threading
import tkinter

# First, establish an ip address for the server
HOST = '10.141.215.186'

# Make sure the port is identical for the server and all clients
PORT = 8080

# Define the length of the messages to be send and received in bytes
HEADER = 1024

# Character encoding style for encoding and decoding messages that are sent/received
STYLE = "utf-8"

# Indicates whether a single client is connected to the server or not
connected = False

def begin_server():
    global connected
    # Create the socket over IPV4 and Transmission Control Protocol (TCP)
    # AF_INET - IPV4
    # SOCK_STREAM - TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
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
            intro_message = "Hello"
            conn.send(intro_message.encode(STYLE));
            while connected:
                # Receive incoming data from client
                data = conn.recv(HEADER)
                # Prevent infinite loop from occurring
                if not data:
                    break
                # Print out the data received in utf-8 formatting
                message = data.decode(STYLE)
                print(f"Client: {message}!")
                # Echo the data back to the client
                conn.send(data)
        print(f"Connection to {addr} lost.")

def main():
    print("Welcome to the Server-Client Application!")
    # Call the function to start the server
    begin_server()

if __name__ == "__main__":
    main()