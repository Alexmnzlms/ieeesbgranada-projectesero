import matplotlib.pyplot as plt
import serial
import time
import numpy as np

ser = serial.Serial('/dev/ttyACM0', 9600)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

x = []
y = []

t0 = time.time()

while True:

#for i in range(10):

    t = time.time() - t0

    print(t)
    print(int(ser.readline()))

    #x.append(t)
    #y.append(int(ser.readline()))
    
    plt.scatter(t, int(ser.readline()))
    plt.show()
    plt.pause(0.001)

