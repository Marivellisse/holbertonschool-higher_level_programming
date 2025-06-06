#!/usr/bin/env python3
"""Client-Server serialization using sockets and JSON"""

import socket
import json


def start_server(host='127.0.0.1', port=65432):
    """Starts a TCP server that receives and deserializes JSON data."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print("Listening on {}:{}".format(host, port))

        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            data = b""
            while True:
                packet = conn.recv(1024)
                if not packet:
                    break
                data += packet
            try:
                msg = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(msg)
            except json.JSONDecodeError:
                print("Invalid JSON received.")


def send_data(d, host='127.0.0.1', port=65432):
    """Connects to the server and sends a JSON-encoded dictionary."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(json.dumps(d).encode('utf-8'))
    except ConnectionRefusedError:
        print("Connection failed.")
