import threading
import socket

HEADER = 64
target_host = "127.0.0.1"
target_port = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

def run(client):
    client.send(str(len(b"index")).encode()+b' ' * (HEADER - len(str(len(b"index")).encode())))
    client.send(b"index")
    size = client.recv(HEADER).decode()
    index = client.recv(int(size)).decode()
    print(index)
    while True:
        req = int(input(f"Select file [0-{len(index.splitlines())-1}]: "))
        client.send(str(len(index.splitlines()[req].encode())).encode()+b' ' * (HEADER - len(str(len(index.splitlines()[req].encode())).encode())))
        client.send(index.splitlines()[req].encode())
        size = client.recv(HEADER).decode()
        if size:
            print(client.recv(int(size)).decode())

run(client)
