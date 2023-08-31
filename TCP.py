import socket

def get_data_from_server(host, port):
    try:
        # Create a socket object
        client_socket = socket.socket()

        # Connect to the server
        client_socket.connect((host, port))

        # # Send an HTTP GET request
        # request = "\r\n"
        # client_socket.sendall(request.encode())

        # Receive and decode the response
        response = b""
        data = client_socket.recv(4096)

        # response += data
        print(data)
        new_data = data.splitlines()
        print( new_data[0])
        new_data[0].strip('q')
        # Close the socket
        client_socket.close()

        # Convert the response bytes to a string
        response_str = response.decode("utf-8")

        return response_str

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    host = "192.168.1.86"
    port = 20001
    response = get_data_from_server(host, port)
    print(response)
