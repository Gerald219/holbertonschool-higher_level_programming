#!/usr/bin/env python3
"""task 4 - client and server using json"""


import socket  # lets computers talk to each other through a network
import json    # turns python data into text and back again


def start_server(host="127.0.0.1", port=65432):
    """open a server that waits, receives json text, and prints the data"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # create socket
        s.bind((host, port))  # connect to address host, port
        s.listen(1)  # wait for one client
        conn, addr = s.accept()  # accept the connection
        with conn:
            data = conn.recv(1024).decode("utf-8")  # read the message
            if data:  # check if message exists
                dictionary = json.loads(data)  # convert json back to dict
                print("received dictionary from client:")
                print(dictionary)  # show the data received


def send_data(dictionary, host="127.0.0.1", port=65432):
    """connect to the server and send dict as json text"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # make socket
        s.connect((host, port))  # connect to the server
        json_data = json.dumps(dictionary)  # turn dict into json text
        s.sendall(json_data.encode("utf-8"))  # send through network
