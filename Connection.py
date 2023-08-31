import socket

host = "192.168.1.86"
port = 20001
def Connect():

    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))
        # print("Connected to {}:{}".format(host, port))
        return "Habilitado"
    except Exception as e:
        print("Error:", e)
        return "Sin Habilitar"

    finally:
        # Close the socket
        client_socket.close()


def Close():
    return "Desconectado"