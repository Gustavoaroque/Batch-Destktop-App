import socket

# Define the server's host and port
server_host = '192.168.1.86'  # Replace with the actual server address or hostname
server_port = 10001             # Replace with the actual port number

# Create a socket object
client_socket = socket.socket()

try:
    # Connect to the server
    client_socket.connect((server_host, server_port))
    print(f"Connected to {server_host}:{server_port}")

    # Send a message to the server
    message = "db.data#1\r\n"
    client_socket.send(message.encode())

    # Receive and display the server's response
    response = client_socket.recv(4096).decode()
    # print(message)
    # response.split('d')
    print(response)

except ConnectionRefusedError:
    print(f"Connection to {server_host}:{server_port} refused.")
finally:
    # Close the client socket
    client_socket.close()
