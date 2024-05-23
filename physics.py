from math import sin, cos, tan, pi, atan2
from marsatm import *
import matplotlib.pyplot as plt

c_ds, v_e, m_zfw, k_v = 4.92, 4400, 699, 0.05
g = 3.71
v_yref = -2
dt = 1


def calc_drag(v, y, data):
    rho = mars_atm(y, data)[1]
    drag = 0.5 * rho * v ** 2 * c_ds
    return drag


def calc_fuel(m_f, delta_t, v_y, m, thruster):
    m_dot = 0
    if thruster and m_f > 0:
        delta_v_y = v_yref - v_y
        if delta_v_y > 0:
            m_dot = m * g / v_e + k_v * delta_v_y
            if m_dot > 5:
                m_dot = 5
            m_f = m_f - m_dot * delta_t
    return m_f, m_dot


def calc_mass(m_f):
    m = m_zfw + m_f
    return m


def calc_thrust(m_d):
    thrust = v_e * m_d
    return thrust


def calc_dv(thrust, drag, m_f):
    m = calc_mass(m_f)
    a = (thrust + drag) / m
    dv = a * dt
    return dv


def velocity(v, angle, dv, delta_t):
    v = v - dv
    v_x = v * cos(angle * pi / 180)
    v_y = v * sin(angle * pi / 180) - g * delta_t
    v_new = (v_x ** 2 + v_y ** 2) ** 0.5
    angle_new = atan2(v_y, v_x) * 180 / pi
    return v_x, v_y, v_new, angle_new


def calc_position(x, y, v_x, v_y, delta_t):
    x = x + v_x * delta_t
    y = y + v_y * delta_t
    return x, y


def list_fill(lst1, x, lst2, y, time_lst, time, v_lst, v, m_dot_lst, m_dot, theta_lst, theta):
    lst1.append(x)
    lst2.append(y)
    time_lst.append(time)
    v_lst.append(v)
    m_dot_lst.append(m_dot)
    theta_lst.append(theta)
    return lst1, lst2, time_lst, v_lst, m_dot_lst, theta_lst

def draw_plot(position_x, position_y, v_lst, m_dot_lst, time_lst, altitude_lst, theta_lst):
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    # Trajectory plot
    axs[0, 0].plot(position_x, position_y)
    axs[0, 0].set_title('Trajectory')
    axs[0, 0].set_xlabel('Horizontal Position (m)')
    axs[0, 0].set_ylabel('Vertical Position (m)')

    # Speed plot
    axs[0, 1].plot(position_x, v_lst)
    axs[0, 1].set_title('Speed')
    axs[0, 1].set_xlabel('Horizontal Position (m)')
    axs[0, 1].set_ylabel('Speed (m/s)')

    # Mass flow rate plot
    axs[0, 2].plot(time_lst, m_dot_lst)
    axs[0, 2].set_title('Mdot vs Time')
    axs[0, 2].set_xlabel('Time (s)')
    axs[0, 2].set_ylabel('Mass Flow Rate (kg/s)')

    # Altitude vs time plot
    axs[1, 0].plot(time_lst, altitude_lst)
    axs[1, 0].set_title('Altitude vs Time')
    axs[1, 0].set_xlabel('Time (s)')
    axs[1, 0].set_ylabel('Altitude (m)')

    # Speed vs time plot
    axs[1, 1].plot(time_lst, v_lst)
    axs[1, 1].set_title('Speed vs Time')
    axs[1, 1].set_xlabel('Time (s)')
    axs[1, 1].set_ylabel('Speed (m/s)')

    # Flight path angle vs time plot
    axs[1, 2].plot(time_lst, theta_lst)
    axs[1, 2].set_title('Gamma vs Time')
    axs[1, 2].set_xlabel('Time (s)')
    axs[1, 2].set_ylabel('Flight Path Angle (degrees)')

    # Adjust layout
    plt.tight_layout()
    plt.show()


def check_thruster(y, h):
    if  0.3 < y < h:
        return True
    else:
        return False