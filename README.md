# ChatSupport
Brings an anonymous resource to anyone who needs support for free and doesn't want to be public about it.
DESCRIPTION:
# Message Format:
* Messages are encoded as strings.
* There is no specific message format enforced in the code, so messages can be any arbitrary text.

# Order of Messages:
* When a peer sends a message, it is broadcasted to all other connected peers.
* The server does not enforce a specific order for message delivery among peers. Messages are sent asynchronously as they are received from clients.

# Actions Taken on Message Transmission and Receipt:
## Transmission:
* When a peer sends a message, it is broadcasted to all other connected peers using the `broadcast` method.
* The message is encoded as a string and sent using the `sendall` method of the socket object associated with each connected peer.
* If an error occurs during message transmission, such as a closed connection or network failure, an error message is printed to the console, indicating the failure to broadcast the message to a specific peer.

## Receipt:
* When a peer receives a message from another peer, it is printed to the console along with the sender's address.
* The received message is decoded from bytes to a string using the `decode` method.
* If an error occurs while receiving a message, such as a closed connection or network failure, an error message is printed to the console, indicating the failure to receive the message from the sender.

# Server Behavior:
* The server listens for incoming connections from peers using the `accept_connections` method.
* When a new connection is accepted, a new thread is spawned to handle messages from the client using the `handle_client_messages` method.
* The server maintains a dictionary of connected peers, where the key is the peer's address and the value is the socket object associated with the peer.
* The server also provides a method to stop the server (`stop` method), which closes all connections and stops listening for new connections.

# Client Behavior:
* The provided code does not include a separate client implementation. Instead, it demonstrates the server-side functionality of handling connections and message broadcasting.

# Usage:
* To use the application, you run the provided code to start the server.
* Once the server is running, it listens for incoming connections from peers.
* Peers can connect to the server and send messages, which will be broadcasted to all other connected peers.
* The example usage at the end of the code demonstrates how to send a message to all peers connected to the server by using the `broadcast` method.
