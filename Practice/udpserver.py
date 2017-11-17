import socket

def Main():
    host='127.0.0.1'
    port=5000
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    print("Server started")
    while True:
        data, address=s.recvfrom(1024)
        data=data.decode('utf-8')
        print("Message from : "+str(address))
        print("From connected user : "+data)
        data=data.upper()
        print("Sending :"+data)
        s.sendto(data.encode('utf-8'),address)
    s.close()

if __name__=='__main__':
    Main()