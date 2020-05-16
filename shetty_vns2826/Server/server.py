#NAME: VIDISHA NARENDRA SHETTY              UTA ID: 1001672826
"""Server for multithreaded chat application."""
from socket import AF_INET, socket, SOCK_STREAM 
from threading import Thread #Import for multithreading
import tkinter #Import for GUI

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True: #Loop waiting for incoming connection
        client, client_address = SERVER.accept() #Server logs the accepted connection 
        print("%s:%s has connected." % client_address) #Prints which client is connected
        client.send(bytes("Greetings from the server! Now type your name and press enter!", "utf8")) #Sends a welcome message to the client that is connected and asks for the user's name
        addresses[client] = client_address #Stores the connected client’s address in the addresses dictionary 
        Thread(target=handle_client, args=(client,)).start() #Handling thread for the connected client is initiated


def handle_client(client):  #Takes client socket as argument.
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8") #Saves the name given by the user
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name #Further instruction to quit the connection
    username[name] = client #Stores the connected client's name in the username dictionary
    client.send(bytes(welcome, "utf8")) 
    notice = 'If you want to send a personal message then type {1to1},{username},your_message_here' #Further instructions for the client to send message only to one other client
    client.send(bytes(notice, "utf8"))
    msg = "%s has joined the chat!" % name #Whenever a new client joins the connection
    broadcast(bytes(msg, "utf8")) #Broadcasts the message to other clients
    clients[client] = name #Stores the client's name in client dictonary

    while True:
        msg = client.recv(BUFSIZ) 
        if bytes("{1to1}", "utf8") in msg: #If {1to1} is present in the msg then the message will be sent to only the desired client
            message = msg.decode("utf-8") 
            temp = message.split(",")[1] #Message after , will be stored in temp
            temp = temp.replace("{","") 
            receiverUsername = temp.replace("}","") 
            temp = message.split(",")[2] #Username of the receiving client is stored in temp
            message = temp #Remaining actual message to be sent is stored in message
            unicast(message,receiverUsername, name+"(1to1): ") #Unicast() is the function to send 1 to 1 message
        if msg != bytes("{quit}", "utf8"): #If the msg doesn't contain {quit} it will broadcast the message to all the connected clients
            
            broadcast(msg, name+"(1toN): ")
        else:
            client.send(bytes("{quit}", "utf8")) 
            client.close() #The client that sends {quit} will be closed
            del clients[client] #Deletes the entry of the client
            broadcast(bytes("%s has left the chat." % name, "utf8")) #Broadcasts that the client has left the chat
            break


def unicast(msg, receiverUsername , prefix=""):  #prefix is for name identification.
    """Unicasts a message to the desired client"""
    for name,socket in username.items(): 
        if receiverUsername == name:
            socket.send(bytes(prefix, "utf-8")+bytes(msg, "utf-8")) #Sends message to the desired client

def broadcast(msg, prefix=""): 
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg) 

def on_closing():
    top.destroy()

"""Dictonaries"""
clients = {}
addresses = {}
username = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
if __name__ == "__main__":
    SERVER.listen(5) #Listens to maximum 5 connections 
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections) #Accepts incoming connections
    ACCEPT_THREAD.start() #Starts the infinite loop
    ACCEPT_THREAD.join()
    client.send (('HTTP/1.1 200 OK').encode('utf-8'))
    message = msg.encode("utf-8")
    client.send(b)
    print("Content-type: text")
    SERVER.close()
