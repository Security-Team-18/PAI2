# serversocket.py

import hashlib
import socket
import hmac

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(2048)
            if(len(data.decode('utf-8'))!=0):
                transf= data.decode('utf-8').split(":")[0]
                resumen=data.decode('utf-8').split(":")[1]
                nonce=data.decode('utf-8').split(":")[2]+"\n"
                verifier= False
                with open("./almacenamiento/nonces.txt", 'r+') as file:
                    lines = file.readlines()
                    if nonce not in lines:
                        file.writelines(nonce)
                    else:
                        print("Transacción con NONCE repetido")
                        verifier= True
                maker=hmac.new(b"1234567890", bytes(transf,"utf-8"), hashlib.sha256)
                digest=maker.hexdigest()
                if(digest==resumen and verifier==False):
                    print("Mensaje íntegro")
                    with open("./almacenamiento/transferencias.txt", 'a+') as f:
                        f.writelines(data.decode('utf-8').split(":")[0])
                else:
                    print("Mensaje no íntegro")
            if not data:
                break
            conn.sendall(data)