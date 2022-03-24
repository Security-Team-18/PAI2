# clientsocket.py

import hashlib
import socket
import hmac
import secrets
import random

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))   
    print("Introduzca la transacción con este formato:")
    valor=input("Cuenta origen, cuenta destino, cantidad\n")
    nonce = secrets.token_urlsafe()
    maker=hmac.new(b"1234567890", bytes(valor,"utf-8"), hashlib.sha256)
    digest=maker.hexdigest()
    s.sendall(bytes(valor+":"+digest+":"+nonce,"utf-8"))
    #s.sendall(bytes(valor+":"+digest+":"+"VdxyP5jtTeOHKdOsNxHcy0Xli2OYTON1VcKtg_1wL7w","utf-8"))

    data = s.recv(2048)

print(f"Received {data!r}")
