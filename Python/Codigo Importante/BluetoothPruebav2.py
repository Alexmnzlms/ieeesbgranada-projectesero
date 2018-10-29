import bluetooth
import time

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(('98:D3:34:90:CA:B8',1))

time.sleep(0.1)

for i in range(50):
    data = sock.recv(4096)
    lista = data.split('\n')
    lista.pop(len(lista)-1)
    lista.pop(0)
    print(lista)
    time.sleep(0.2)
    
sock.close()
