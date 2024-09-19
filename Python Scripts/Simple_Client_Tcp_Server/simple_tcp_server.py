import socket

def tcp_server(host):
    # 1.) create a socket Object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.socket is used mainly for communication between devices 
    # socket.AF_INET is used for IPv4 addresses, if we what IPv6 we would use socket.AF_INET6
    # socket.SOCK_STREAM is used for TCP connections, if we wanted UDP we would use socket.SOCK_DGRAM
    # So we expect a TCP connection over IPv4
    port = 12345 
    # 2.) bind the socket to an address and port
    server_socket.bind((host,port))
    # random port number
    # 3.) listen for incoming connections
    server_socket.listen(5)
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print("Connection established!")

        # Send a welcome message
        message = "Hello, client! Welcome to the server."
        client_socket.send(message.encode('utf-8'))

        # Close the connection
        client_socket.close()
    # listen for incoming connections, the argument is the maximum number of queued connections
tcp_server('localhost') # Call the function to start the server 
# Note: This code will not run successfully as is, as there are some missing parts and errors.
