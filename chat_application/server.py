import socket
import threading

HOST = '127.0.0.1'
PORT =  2345
listener_limit = 5
active_clients = []

def listen_for_messages(client, username):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                print(f"Received message from {username}: {message}")
                final_msg = f"{message}"
                send_messages_to_all(username, final_msg)
            else:
                print(f"The message sent from Client {username} is empty")
        except Exception as e:
            print(f"Error while receiving message from {username}: {e}")
            break


def send_messages_to_client(client, message):
    client.sendall(message.encode())

def send_messages_to_all(from_username, message):
    for user in active_clients:
        print(f"Sending message to {user[0]}: {message}")
        send_messages_to_client(user[1], f"{from_username}~{message}")


def client_handler(client):
    while True:
        try:
            username = client.recv(2048).decode('utf-8')
            if username != '':
                active_clients.append((username, client))
                prompt_message = f"{username} added to the chat"
                send_messages_to_all("SERVER", prompt_message)
                break
            else:
                print("Client username is empty")
        except Exception as e:
            print(f"Error while handling client: {e}")
            break

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Running the server {HOST} {PORT}")
    except Exception as e:
        print(f"Unable to bind to host {HOST} and port {PORT}: {e}")
        return

    server.listen(listener_limit)

    while True:
        try:
            client, address = server.accept()
            print(f"Succesfully connected to Client {address[0]} {address[1]}")
            threading.Thread(target=client_handler, args=(client, )).start()
        except Exception as e:
            print(f"Error accepting Client connection: {e}")

if __name__ == '__main__':
    main()
