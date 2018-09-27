import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import time
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
line, = ax1.plot([],[],lw=2)

ser = serial.Serial('/dev/ttyACM0',9600)

t0 = time.time()

def init():
    line.set_data([],[])
    return line,

def graf(i):
    
    x = time.time() - t0
    ser.reset_input_buffer()
    y = int(ser.readline())
    line.set_data(x,y)
    return line,

ani = animation.FuncAnimation(fig, graf, init_func = init, interval = 20, blit=True)
plt.show()
