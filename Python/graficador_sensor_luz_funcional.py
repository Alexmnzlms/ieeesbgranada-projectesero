################################################################################
# Autor: Carlos Lara Casanova
#
# Programa que grafica una serie de valores dados desde un Arduino
# conectado mediante USB 
#
################################################################################

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import numpy as np
import time
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
ser2 = serial.Serial('/dev/ttyACM1',9600)

matplotlib.rcParams['toolbar'] = 'None'

fig = plt.figure()
fig.patch.set_color('gray')
ax = fig.add_subplot(211)
plt.yticks([])
plt.xticks([])

ax2 = fig.add_subplot(212)
plt.yticks([])
plt.xticks([])

line, = ax.plot([],[],lw=2)
line2, = ax2.plot([],[],lw=2, color='red')

fig.set_animated(True)
fig.patch.set_animated(True)
ax.patch.set_animated(True)

j = 0
dato = 0
dato2 = 0

line.set_data([],[])
line2.set_data([],[])


def animate(i):

    global j
    global dato
    global dato2

    x = line.get_xdata()
    y = line.get_ydata()
    x2 = line2.get_xdata()
    y2 = line2.get_ydata()
    
    j = time.clock()

    try:
        dato = int(ser.readline())
        dato2 = int(ser2.readline())
    except:
        pass


    ser.reset_input_buffer()
    ser2.reset_input_buffer()

    x.append(j)
    y.append(dato)

    x2.append(j)
    y2.append(dato2)
    
    line.set_data(x,y)
    line2.set_data(x2,y2)
    
    ax.relim()
    ax.autoscale()

    ax2.relim()
    ax2.autoscale()

    return line,line2,

ani = animation.FuncAnimation(fig, animate, interval = 1, blit = True)

plt.show()
