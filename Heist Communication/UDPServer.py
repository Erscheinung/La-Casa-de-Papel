import socket
import base64

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))


print("UDP server up and listening")
# Listen for incoming datagrams


# MESSAGE
heistInstruction = "Black lives don't matter."
InstructionToSend = ""

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    fibo1 = 0
    fibo2 = 1
    fiboN = 0
    # DECODING MESSAGE RECEIVED FROM THE TEAM
    message = bytesAddressPair[0]
    message = base64.b64decode(message).decode('utf-8')

    finalMessage = ""
    for i in range(0,len(message)):
        if i<=1:
            fiboN = 0
        else:
            fiboN = fibo1 + fibo2
            fibo1 = fibo2
            fibo2 = fiboN
        finalMessage = finalMessage + chr(ord(message[i])-fiboN)
        
    address = bytesAddressPair[1]
    teamMsg = "Message from your Team:{}".format(finalMessage)
    teamIP  = "Team IP Address:{}".format(address)
    print(teamMsg)
    print(teamIP)
    
    
    # ENCODING MESSAGE TO SEND TO THE TEAM
    fibo1 = 0
    fibo2 = 1
    fiboN = 0

    for i in range(0,len(heistInstruction)):
        if i<=1:
            fiboN = 0
        else:
            fiboN = fibo1 + fibo2
            fibo1 = fibo2
            fibo2 = fiboN
        InstructionToSend = InstructionToSend + chr(ord(heistInstruction[i])+fiboN)
    
    instructionBytes = InstructionToSend.encode('utf-8')
    instructionBytes = base64.b64encode(instructionBytes)

    # Sending a reply to client
    UDPServerSocket.sendto(instructionBytes, address)