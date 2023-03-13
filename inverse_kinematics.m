clear
close all

%Defining Cartesian Coordinates
x=[-6 -5 -4 -2 0 2 4 5 6 5 4 2 0 -2 -4 -5 -6]; 
y=[-13 -14 -14.5 -15 -15 -15 -15 -15.5 -16 -16 -16 -16 -16 -16 -16 -16 -16];

% Joint Lengths
L1=7;
L2=13;

theta1 = []; % Initialize empty array for theta1
theta2 = []; % Initialize empty array for theta2


% Loop through each target point and calculate the joint angles
for i = 1:length(x)
    x1 = x(i); % Target x-coordinate
    y1 = y(i); % Target y-coordinate

    % Calculate the inverse kinematics
     L3=x1^2 + y1^2;
     theta2_i = acos((L3- L1^2 - L2^2)/(2*L1*L2));
     theta1_i = atan2(y1,x1) - atan2((L2*sin(theta2_i)),(L1 + L2*cos(theta2_i)));
     
     theta1 = [theta1, theta1_i*(180/pi)]; % Append theta1_i to theta1
     theta2 = [theta2, theta2_i*(180/pi)]; % Append theta2_i to theta2
end

% Plotting the Legs Trajectory
figure;

for i = 1:length(theta1)
    x = L1*cosd(theta1(i));
    y = L1*sind(theta1(i));

    x1 = L2*cosd(theta1(i)+theta2(i));
    y1 = L2*sind(theta1(i)+theta2(i));

    x2 = x + x1;
    y2 = y + y1; 

    plot([0,x],[0,y],'-', ... 
        [x, x2],[y, y2],'-')
    xlim([-10 10])
    ylim([-20 5])
    title("Leg Path")
    drawnow;
    pause(0.2);
end



