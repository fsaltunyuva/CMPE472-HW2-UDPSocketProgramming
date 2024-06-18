import socket


def create_client():
    localIP = socket.gethostname()  # Local IP address
    localPort = 7000  # Specific port number(can be changed)
    bufferSize = 1024  # Buffer size

    # Get user input for the port number for the client
    port = int(input("Enter the port number for the client: "))

    try:

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket

        client_socket.bind((localIP, port))  # Bind the socket to localhost and a specific port

        while True:

            message = input("Enter a message: ")  # Get user input for the message

            client_socket.sendto(message.encode(), (localIP, localPort))  # Send the message to the server

            response = client_socket.recvfrom(bufferSize)  # Receive the server's response

            print(response[0].decode())  # Print the server's response

            # Check if the server's response is "Port is not allowed to communicate"
            if response[
                0].decode() == "Port is not allowed to communicate":  # If the response is "Port is not allowed to communicate" then break the loop
                client_socket.close()
                break

    except socket.error as e:
        print("Error:", e)


def main():
    create_client()


if __name__ == "__main__":
    main()

