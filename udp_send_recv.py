
import socket
import struct

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def PrintHex(str2Print):
    print("      ",end='')
    for i in range(0,16):  
        print("%3s " % hex(i),end='')
    print()
    print("      ",end='')
    for i in range(0,16):  
        print("%-3s " % "#",end='')
    print()
    index = 0
    len_str = len(str2Print)
    print('0x%02x  '%index,end='')
    while index < len_str:  
        temp=str2Print[index]  
        print('%02x  '%temp,end='')
        index=index+1  
        if index % 16 == 0:  
            print('')  
            print('0x%02x  '%index,end='')


if __name__ == '__main__':
    #while True:
    msg = [0x3e, 0x00, 0x47, 0x02, 0x04, 0x05, 0x00, 0x09, \
           0x00, 0x01, 0x00, 0x6d, 0xe1, 0x00, 0x00, 0x0f, \
           0xc9, 0x26, 0xd2, 0x37, 0x22, 0x8f, 0xe0, 0x3f, \
           0x1a, 0x2e, 0xd8, 0x8e, 0xfd, 0xf4, 0xd4, 0x7d, \
           0xa3, 0x06, 0x01, 0x00, 0x00, 0x69, 0x93, 0x16, \
           0x75, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, \
           0x00, 0x07, 0xdf, 0x00, 0x0a, 0x00, 0x0c, 0x00, \
           0x01, 0x00, 0x04, 0x00, 0x05, 0x00, 0x00, 0x24, \
           0xa4, 0x00, 0x00, 0x00, 0x00, 0x1a, 0x68]

    date=struct.pack("%dB"%(len(msg)),*msg)

    server_address = ("58.251.112.221", 8000) 
    client_socket.sendto(date, server_address) 

    receive_data, sender_address = client_socket.recvfrom(1024)
    #print(sender_address)
    PrintHex(receive_data)