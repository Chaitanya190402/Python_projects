# Messenger Client and Server

This project consists of a simple messenger application with a client and server implemented in Python. The client provides a graphical user interface (GUI) for users to send and receive messages, while the server manages the communication between clients.

## Messenger Client

### Requirements
- Python 3.x
- Tkinter (`pip install tk`)
- Socket

### Usage
1. Run the script: `python messenger_client.py`.
2. Enter a username in the provided textbox.
3. Click the "Join" button to connect to the server.
4. Use the text entry at the bottom to type your messages.
5. Click the "Send" button or press Enter to send messages.
6. The chat history is displayed in the central scrolled text box.

### Notes
- The client GUI is built using Tkinter.
- Messages are sent to the server, which broadcasts them to all connected clients.
- The client script uses threading to handle message reception without blocking the GUI.

## Messenger Server

### Requirements
- Python 3.x
- Socket
- Threading

### Usage
1. Run the script: `python messenger_server.py`.
2. The server listens for incoming connections on the specified host and port.
3. Clients can connect to the server and join the chat.

### Notes
- The server manages multiple client connections using threading.
- Messages sent by clients are broadcasted to all connected clients.
- The server script includes basic error handling.

## Troubleshooting
- Ensure that the required dependencies are installed (`tkinter`, `socket`, `threading`).
- Check for any error messages in the console.

Feel free to customize and extend the scripts according to your needs. Happy messaging!
