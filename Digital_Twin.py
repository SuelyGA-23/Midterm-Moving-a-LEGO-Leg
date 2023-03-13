import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
from math import cos, sin, radians

IP = "10.245.155.24"
Port = 1883

theta1 = []
theta2 = []

# Define the callback function to handle incoming messages
def on_message(client, userdata, message):
    global theta1, theta2
    angles = str(message.payload.decode())
    angles = angles.replace('(', '').replace(')', '').split(',')
    theta1.append(radians(float(angles[0])))
    theta2.append(radians(float(angles[1])))

sully = mqtt.Client("sad2")
sully.on_message = on_message  # Set the callback function for incoming messages

sully.connect(IP, Port)
sully.subscribe("angles")  # Subscribe to the 'angles' topic

# Start the MQTT client's network loop
sully.loop_start()

L1 = 7
L2 = 13

fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(16):
    while len(theta1) < i+1:
        plt.pause(0.1)  # Wait for new messages to arrive
    x = L1 * cos(theta1[i])
    y = L1 * sin(theta1[i])

    x1 = L2 * cos(theta1[i] + theta2[i])
    y1 = L2 * sin(theta1[i] + theta2[i])

    x2 = x + x1
    y2 = y + y1

    ax.clear()  # Clear the previous plot to update it with the new values
    ax.plot([0, x], [0, y], '-', [x, x2], [y, y2], '-')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-20, 20])
    ax.set_title("Leg Path")
    plt.draw()
    plt.pause(0.1)  # Pause briefly to allow the plot to update

plt.show()







