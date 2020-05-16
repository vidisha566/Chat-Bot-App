#!/usr/bin/env python3
"""Script for GUI chat client 1."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter #Import for GUI 

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8") #Decodes message received from server
            if '{1to1}' not in msg: 
            	msg_list.insert(tkinter.END, msg) #Displays the list of messages on the screen
            elif 'If you want to send a personal message' in msg: 
            	msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get() #Message that has to be sent is extracted
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        top.destroy()

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")    #Sets the input field to {quit} and then calls send()
    send()

top = tkinter.Tk()
top.title("Client") #Sets the title of GUI

messages_frame = tkinter.Frame(top) #message list will be stored in messages_frame
my_msg = tkinter.StringVar()  # For the messages to be sent.
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=80, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)  #Binding the send button so that whenever the send button is pressed the message is sent to the server
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)
"""Closes the window"""

#----Now comes the sockets part----
HOST = '127.0.0.1'
PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.