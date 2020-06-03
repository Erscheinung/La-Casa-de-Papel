import socket
import base64

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# MESSAGE TO THE PROFESSOR
teamResponse = "Ok Boomer"
teamResponseToSend = ""

# ENCODING MESSAGE TO SEND TO THE PROFESSOR
fibo1 = 0
fibo2 = 1
fiboN = 0

for i in range(0,len(teamResponse)):
    if i<=1:
        fiboN = 0
    else:
        fiboN = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fiboN
    teamResponseToSend = teamResponseToSend + chr(ord(teamResponse[i])+fiboN)

responseBytes = teamResponseToSend.encode('utf-8')
responseBytes = base64.b64encode(responseBytes)

# Send to server using created UDP socket
UDPClientSocket.sendto(responseBytes, serverAddressPort)

# DECODING MESSAGE RECEIVED FROM THE PROFESSOR
heistInstructions = UDPClientSocket.recvfrom(bufferSize)
InstructionMessage = heistInstructions[0]

decodedMessage = base64.b64decode(InstructionMessage).decode('utf-8')


fibo1 = 0
fibo2 = 1
fiboN = 0

finalMessage = ""
for i in range(0,len(decodedMessage)):
    if i<=1:
        fiboN = 0
    else:
        fiboN = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fiboN
    finalMessage = finalMessage + chr(ord(decodedMessage[i])-fiboN)

msg = "Message from the Professor: {}".format(finalMessage)
print(msg)



