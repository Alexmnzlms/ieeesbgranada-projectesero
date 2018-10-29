import bluetooth
import time

print("conectando")
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(('98:D3:34:90:CA:B8',1))
print("conectado")

time.sleep(0.1)

lista = []

for i in range(50):
    print("leer")
    data = sock.recv(1024)
    if not data:
        break
    print(data)
    lista.append(data)
    #lista.pop(len(lista)-1)
    #lista.pop(0)
    time.sleep(0.2)
    
sock.close()

print(lista)
