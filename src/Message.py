import socket
import threading

class PeerToPeerChat:
    def __init__(self):
        # Initialize socket for peer communication
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '0.0.0.0'  # Allow connections from any interface
        self.port = 8090  # Default port for communication
        self.peers = {}  # Dictionary to store connected peers

    def start(self):
        # Bind the socket to the host and port
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)  # Listen for incoming connections
        print("Server started. Waiting for connections...")

        # Thread to handle incoming connections
        threading.Thread(target=self.accept_connections).start()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.socket.accept()
            print(f"Connection from {client_address}")
            # Add client to peers dictionary
            self.peers[client_address] = client_socket
            # Thread to handle messages from the client
            threading.Thread(target=self.handle_client_messages, args=(client_socket, client_address)).start()

    def handle_client_messages(self, client_socket, client_address):
        while True:
            try:
                # Receive message from client
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"Received message from {client_address}: {message}")
                # Forward message to all other peers
                self.broadcast(message, client_address)
            except Exception as e:
                print(f"Error handling message from {client_address}: {e}")
                break

        # Remove client from peers dictionary and close connection
        del self.peers[client_address]
        client_socket.close()
        print(f"Connection closed with {client_address}")

    def broadcast(self, message, sender_address):
        # Send message to all peers except the sender
        for address, socket in self.peers.items():
            if address != sender_address:
                try:
                    socket.sendall(message.encode())
                except Exception as e:
                    print(f"Error broadcasting message to {address}: {e}")

    def send_message(self, receiver_address, message):
        # Send message to a specific peer
        if receiver_address in self.peers:
            try:
                self.peers[receiver_address].sendall(message.encode())
                print(f"Message sent to {receiver_address}: {message}")
            except Exception as e:
                print(f"Error sending message to {receiver_address}: {e}")
        else:
            print(f"Peer {receiver_address} not found.")

    def stop(self):
        # Close all connections and stop the server
        for socket in self.peers.values():
            socket.close()
        self.socket.close()
        print("Server stopped.")

if __name__ == "__main__":
    chat_server = PeerToPeerChat()
    chat_server.start()

    # Example usage
    while True:
        message = input("Enter message: ")
        chat_server.broadcast(message, None)  # Broadcast message to all peers
