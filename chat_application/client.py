import socket
import threading
import tkinter as tk    
from tkinter import scrolledtext
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 2345

DARK_GREY = '#121211'
MEDIUM_GREY = '#1f1b24'
WHITE = "white"
OCEAN_BLUE = '#464EB8'
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def add_message(message):
    root.after(0, _add_message, message)


def _add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)


def connect():
    username = user_textbox.get()
    if username != '':
        try:
            Client.connect((HOST, PORT))
            print("Successfully connected to server")
            add_message("[SERVER] Successfully connected to the server")
            print(f"Sending username to server: {username}")
            Client.sendall(username.encode())
            threading.Thread(target=listen_from_messages_from_server, args=(Client,)).start()
            user_textbox.config(state=tk.DISABLED)
            user_button.config(state=tk.DISABLED)
            root.after(100, lambda: add_message(f"[SERVER] {username} joined the chat"))
        except Exception as e:
            messagebox.showerror("Unable to connect to server", f"Unable to connect server {HOST} {PORT}: {e}")
            exit(0)
    else:
        messagebox.showerror("Invalid username", "Username cannot be empty")


def send_message():
    message = Message_TextBox.get()
    username = user_textbox.get()

    if message != '' and username != '':
        full_message = f"{message}"
        Client.sendall(full_message.encode())
        Message_TextBox.delete(0, tk.END)
    else:
        messagebox.showerror("Empty message", "Message or username cannot be empty")


def listen_from_messages_from_server(Client):
    while True:
        try:
            message = Client.recv(2048).decode('utf-8')
            if message != '':
                parts = message.split("~", 1)
                if len(parts) == 2:
                    username, content = parts
                    add_message(f"[{username}] {content}")
                else:
                    print(f"Invalid message format: {message}")
            else:
                messagebox.showerror("Error", "Message received from server is empty")
        except Exception as e:
            print(f"Error while receiving message from server: {e}")
            break


root = tk.Tk()
root.geometry("600x600")
root.title("Messenger Client")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

top_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width=600, height=400, bg=MEDIUM_GREY)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

user_label = tk.Label(top_frame, text="Enter username : ", font=FONT, bg=DARK_GREY, fg=WHITE)
user_label.pack(side=tk.LEFT, padx=10)

user_textbox = tk.Entry(top_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
user_textbox.pack(side=tk.LEFT)

user_button = tk.Button(top_frame, text="join", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect)
user_button.pack(side=tk.LEFT, padx=19)

Message_TextBox = tk.Entry(bottom_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=38)
Message_TextBox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(bottom_frame, text="Send", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


def main():
    root.mainloop()


if __name__ == '__main__':
    main()
