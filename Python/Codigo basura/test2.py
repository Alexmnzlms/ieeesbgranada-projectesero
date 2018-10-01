import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

x = []
y = []

fig = plt.Figure()
ax1 = fig.add_subplot(1,1,1)

ax1.grid(True)

def graficar(i):

    x.append(1)
    y.append(2)

    ax1.clear()
    ax1.plot(x,y)

ani = animation.FuncAnimation(fig, graficar,blit=True)
plt.show()
