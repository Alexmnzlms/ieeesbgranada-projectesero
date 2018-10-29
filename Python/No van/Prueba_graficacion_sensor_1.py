################################################################################
# Autor: Alejandro Manzanares
# Prueba de graficacion con los datos obtenidos con el sensor barato concetado
# al arduino (el que no tiene placa)
################################################################################

import matplotlib.pyplot as plt
import numpy as np
import serial

################################################################################

ser = serial.Serial('/dev/ttyACM0',9600)
plt.ion() ## Note this correction
fig = plt.figure()
plt.axis([0,1000,0,1])

i = 0
x = list()
y = list()

ser.readline()

while i < 10:
    temp_y = int(ser.readline());
    x.append(i);
    y.append(temp_y);
    plt.scatter(i,temp_y);
    i += 1;
    plt.show()
    plt.pause(0.0001) #Note this correction

################################################################################
