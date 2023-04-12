# DUAL PENDULUM SIMULATION USING PYTHON AND GRAPHICS.PY
# I'M USING LAGRANGIAN FORMULATION TO NUMERICALLY CALCULATE THE PENDULUM PATH AND VELOCITY
# REFERENCE: diego.assencio.com/?index=1500c66ae7ab27bb0106467c68feebc6
# AMIR MONFARED | DEC 2019 | TWITTER: @AMONFARED73
# TEHRAN, IRAN

from graphics import *
import math
import numpy as geek

# GLOBAL VARIABLES
num = 10000  # NUMBER OF DATA SETS
m1 = 1  # MASS 1 [Kg]
m2 = 1  # MASS 2 [Kg]
l1 = 1  # LENGTH 1 [m]
l2 = 1  # LENGTH 2 [m]
g = 10  # GRAVITY CONST [m/s^2]
dt = 0.01  # TIME STEP SIZE [s]

# CANONICAL X AND P PARAMETERS
theta1 = [0.0] * num  # ANGLE 1 [Rad]
theta2 = [0.0] * num  # ANGLE 2 [Rad]
theta1_dot = [0.0] * num  # ANGULAR VELOCITY 1 [Rad/s]
theta2_dot = [0.0] * num  # ANGULAR VELOCITY 2 [Rad/s]
theta1_double_dot = [0.0] * num  # ANGULAR ACCELERATION 1 [Rad/s^2]
theta2_double_dot = [0.0] * num  # ANGULAR ACCELERATION 2 [Rad/s^2]

# INITIAL CONDITIONS
theta1[0] = math.pi / 2 + math.pi / 3
theta2[0] = -math.pi / 2
theta1_dot[0] = 0
theta2_dot[0] = 5
theta1_double_dot[0] = 0
theta2_double_dot[0] = 0

# LOCATION OF BALL IN XY COORDINATE
loc1 = geek.zeros([num, 2])
loc2 = geek.zeros([num, 2])
loc1[0][0] = l1 * math.sin(theta1[0])
loc1[0][1] = -l1 * math.cos(theta1[0])
loc2[0][0] = l1 * math.sin(theta1[0]) + l2 * math.sin(theta2[0])
loc2[0][1] = -l1 * math.cos(theta1[0]) - l1 * math.cos(theta2[0])

# CALCULATION LOOP
i = 1
while i < num:
    alpha1 = (l2 / l1) * (m2 / (m1 + m2)) * math.cos(theta1[i - 1] - theta2[i - 1])
    alpha2 = (l1 / l2) * math.cos(theta1[i - 1] - theta2[i - 1])
    f1 = -(l2 / l1) * (m2 / (m1 + m2)) * math.pow(theta2_dot[i - 1], 2) * math.sin(theta1[i - 1] - theta2[i - 1]) - (
            g / l1) * math.sin(theta1[i - 1])
    f2 = (l1 / l2) * math.pow(theta1_dot[i - 1], 2) * math.sin(theta1[i - 1] - theta2[i - 1]) - (g / l2) * math.sin(
        theta2[i - 1])
    theta1_double_dot[i] = (1 / (1 - alpha1 * alpha2)) * (f1 - alpha1 * f2)
    theta2_double_dot[i] = (1 / (1 - alpha1 * alpha2)) * (f2 - alpha2 * f1)
    theta1_dot[i] = theta1_double_dot[i] * dt + theta1_dot[i - 1]
    theta2_dot[i] = theta2_double_dot[i] * dt + theta2_dot[i - 1]
    theta1[i] = theta1_dot[i] * dt + theta1[i - 1]
    theta2[i] = theta2_dot[i] * dt + theta2[i - 1]
    loc1[i][0] = l1 * math.sin(theta1[i])
    loc1[i][1] = -l1 * math.cos(theta1[i])
    loc2[i][0] = l1 * math.sin(theta1[i]) + l2 * math.sin(theta2[i])
    loc2[i][1] = -l1 * math.cos(theta1[i]) - l1 * math.cos(theta2[i])
    i += 1


# FUNCTION TO RETURN A LINE THAT CONNECTS TWO BALLS
def line(x1, y1, x2, y2):
    return Line(Point(x1, y1), Point(x2, y2))


# FUNCTION TO GENERATE CIRCLES
def c(x, y, r):
    return Circle(Point(x, y), r)


# MAIN FUNC
def main():
    win = GraphWin("Double Pendulum Simulation", 600, 500, autoflush=False)
    title = Text(Point(73, 12), "Double Pendulum")
    title.setStyle("bold")
    title.draw(win)
    cir = Circle(Point(300, 200), 5)
    cir.setFill("black")
    cir.draw(win)
    for j in range(num):
        circle_1 = c(100 * loc1[j][0] + 300, -100 * loc1[j][1] + 200, 20)
        circle_1.setFill("red")
        circle_2 = c(100 * loc2[j][0] + 300, -100 * loc2[j][1] + 200, 20)
        circle_2.setFill("blue")
        line_0 = line(300, 200, 100 * loc1[j][0] + 300, -100 * loc1[j][1] + 200)
        line_0.setWidth(3)
        line_1 = line(100 * loc1[j][0] + 300, -100 * loc1[j][1] + 200, 100 * loc2[j][0] + 300, - 100 * loc2[j][1] + 200)
        line_1.setWidth(3)

        line_0.draw(win)
        line_1.draw(win)
        circle_1.draw(win)
        circle_2.draw(win)

        update(60)

        circle_1.undraw()
        circle_2.undraw()
        line_0.undraw()
        line_1.undraw()
    win.getMouse()
    win.close()


main()
