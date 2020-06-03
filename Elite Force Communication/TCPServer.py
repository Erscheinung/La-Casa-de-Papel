import socket

HOST = '127.0.0.1'  
PORT = 4000       

negotiationDemands = "four ice-cream sundaes and a helicopter"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('Received by the Professor: ',data.decode("utf-8"))
            if not data:
                break
            conn.send(bytes(negotiationDemands,"utf-8"))
            print('Sent by the Professor: ',negotiationDemands)
