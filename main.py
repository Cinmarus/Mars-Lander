from physics import *

h, v, theta = 20000, 262, -20
h_t = 1800
m_f = 80
dt = 0.1
time = 0
dv = 0
atm_data = marsinit()
thruster = False

position_x = [0]
position_y = [20000]
time_lst = [0]
v_lst = [262]
theta_lst = [-20]
m_dot_lst = [0]


x = 0
y = 20000

v_x = v * cos(theta * pi / 180)
v_y = v * sin(theta * pi / 180)

print(v_x, v_y)

while y > 0:
    thruster = check_thruster(y, h_t)
    drag = calc_drag(v, y, atm_data)
    m = calc_mass(m_f)
    m_f, m_dot = calc_fuel(m_f, dt, v_y, m_zfw, thruster)
    thrust = calc_thrust(m_dot)
    dv = calc_dv(thrust, drag, m_f, dt)
    v_x, v_y, v, theta = velocity(v, theta, dv, dt)
    x, y = calc_position(x, y, v_x, v_y, dt)
    if y > 0:
        list_fill(position_x, x, position_y, y, time_lst, time, v_lst, v, m_dot_lst, m_dot, theta_lst, theta)
    time += dt
    print(v, y)


draw_plot(position_x, position_y, v_lst, m_dot_lst, time_lst, position_y, theta_lst)





