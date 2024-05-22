from math import sin, cos, tan, pi
import matplotlib.pyplot as plt
from marsatm import *
from physics import *

h, v, theta = 20000, -262, -20
m_f = 100
dt = 1
time = 0
dv = 0
atm_data = marsinit()
thruster = False

position_x = [0]
position_y = [20000]

x = 0
y = 20000

v_x = v * cos(theta * pi / 180)
v_y = v * sin(theta * pi / 180)

print(v_x, v_y)

while y > 0:
    v_x, v_y, v, theta = velocity(v, theta, dv, dt)
    drag = calc_drag(v, y, atm_data)
    m_f, m_dot = calc_fuel(m_f, dt, v_y, m_zfw, thruster)
    m = calc_mass(m_f)
    thrust = calc_thrust(m_dot)
    dv = calc_dv(thrust, drag, m_f)
    x, y = calc_position(x, y, v_x, v_y, dt)
    position_x.append(x)
    position_y.append(y)
    time += dt

plt.plot(position_x, position_y)
plt.show()





