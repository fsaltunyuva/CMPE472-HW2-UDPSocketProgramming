import socket


def create_server():
    localIP = socket.gethostname()  # Local IP address
    localPort = 7000  # Specific port number(can be changed)
    bufferSize = 1024  # Buffer size

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket

    server_socket.bind((localIP, localPort))  # Bind the socket to localhost and a specific port

    permitted_numbers = []  # List to keep track of the permitted numbers

    clients = []  # List to keep track of the clients

    try:  # Try block to catch exceptions
        while True:  # Keep the server running
            bytesAddressPair = server_socket.recvfrom(bufferSize)  # Receive the message and the client's address
            message = bytesAddressPair[0]  # Extract the message
            client_address = bytesAddressPair[1]  # Extract the client's address

            if client_address not in clients:  # Check if the client is already in the list
                clients.append(client_address)  # Add the client to the list

            print("Message: ", message.decode())  # Print the message
            print("Client Address: ", client_address)  # Print the client's address

            lower_case_message = message.decode().lower()  # Convert the message to lowercase

            # Check the client's port and process the message accordingly
            if client_address[1] == 1234:
                if lower_case_message.startswith("permission"):
                    number = lower_case_message.strip("permission").strip()
                    if number.isdigit():
                        number = int(number)
                        if number not in permitted_numbers:
                            permitted_numbers.append(number)
                            server_socket.sendto("Permission Accepted".encode(), client_address)
                        else:
                            server_socket.sendto("Already Permitted".encode(), client_address)
                    else:
                        server_socket.sendto("Invalid Message".encode(), client_address)
                else:
                    server_socket.sendto("Invalid Message".encode(), client_address)
            elif client_address[1] == 3333:
                if lower_case_message.startswith("request"):
                    number = lower_case_message.strip("request").strip()
                    if number.isdigit():
                        number = int(number)
                        if number in permitted_numbers:
                            server_socket.sendto("Request Accepted".encode(), client_address)
                        else:
                            server_socket.sendto("Request Rejected".encode(), client_address)
                    else:
                        server_socket.sendto("Invalid Message".encode(), client_address)
                else:
                    server_socket.sendto("Invalid Message".encode(), client_address)
            else:
                server_socket.sendto("Port is not allowed to communicate".encode(), client_address)

            # Check if the number of connected clients is 4
            if len(clients) == 4:  # If the number of connected clients is 4 then break the loop
                print("The number of connected clients is 4.")
                break

    except socket.error as e:
        print("Error:", e)
    finally:
        server_socket.close()  # Close the server socket


def main():
    create_server()  # Call the create_server function


if __name__ == "__main__":
    main()
