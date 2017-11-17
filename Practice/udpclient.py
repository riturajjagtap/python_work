import socket

def Main():
    host='127.0.0.1'
    port=5001
    server=('127.0.0.1',5000)
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    msg=input("Enter message: ")
    while msg!='q':
        s.sendto(msg.encode('utf-8'),server)
        data,address=s.recvfrom(1024)
        data=data.decode('utf-8')
        print("Received from server: "+data)
        msg = input("Enter message: ")
    s.close()

if __name__=='__main__':
    Main()
