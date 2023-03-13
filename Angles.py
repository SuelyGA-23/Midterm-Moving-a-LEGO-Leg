import paho.mqtt.client as mqtt
import time

theta1=[-179.6848, -170.6227, -165.1205, -156.6310 , -150.0000,  -131.2383,  -122.5505, -113.4747, -119.3291, -124.7926, -134.5462, -142.6168, -148.7962,  -152.8651, -154.0372, -154.5868]
theta2=[94.0960, 89.0555, 87.4019 ,86.5350, 87.7958 ,82.7399, 74.9528 ,66.0090 ,69.7478, 72.7403, 76.6576 ,77.9485  ,76.6576 ,72.7403 ,69.7478 ,66.0090]


IP="10.245.155.186"
Port= 1883

sully=mqtt.Client("sad")

sully.connect(IP,Port)

topic="angles"

sully.loop_start()  # Start the MQTT loop

for i in range(16):
    x = theta1[i]
    y = theta2[i]
    shoulder = x
    elbow = y
    shoulder = float(x)
    elbow = float(y)
    sully.publish(topic, f"({shoulder},{elbow})")
    time.sleep(1)

sully.loop_stop()  # Stop the MQTT loop
sully.disconnect() 




