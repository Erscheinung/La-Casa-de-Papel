import socket

HOST = '127.0.0.1'  
PORT = 4000        

negotiationTeamResponse = "no u"
print("lol")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.send(bytes(negotiationTeamResponse,"utf-8"))
        print('Sent by the negotiation Team: ',negotiationTeamResponse)
        data = s.recv(1024)
        

print('Received by the negotiation Team: ', data.decode("utf-8"))