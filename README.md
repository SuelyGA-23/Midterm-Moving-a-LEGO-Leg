# Midterm-Moving-a-LEGO-Leg
Code to Move a LEGO Car via MQTT Communication 

inverse_kinematics_m-- Matlab code that takes in cartesian coordinates (x,y) and performs the inverse kinematics of a 2 link system to get corresponding theta values. It then plots the 2-link's trajectory.
angles2.py -- Python code that takes in theta values and publishes them to a MQTT Broker topic called "angles"
Digital_Twin2.py -- Python code that subscribes to a MQTT Broker topic called "angles" and takes the angles and plots its current postion. 
