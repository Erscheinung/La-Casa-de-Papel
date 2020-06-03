import base64

f = open("capturedText.txt","r")

fibo1=0
fibo2=1
fiboN=0

string = ""

while True:
    char = f.read(1)
    string += char
    if not char:
        break
    
message = base64.b64decode(string).decode('utf-8')
decodedMessage = ""

for i in range(len(message)):
    if i<=1:
        fiboN = 0
    else:
        fiboN = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fiboN
    decodedMessage = decodedMessage + chr(ord(message[i])-fiboN)
    
print(decodedMessage)