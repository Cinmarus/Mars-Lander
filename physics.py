from math import sin, cos, tan, pi
from marsatm import *

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
    if thruster:
        delta_v_y = v_yref - v_y
        m_dot = m * g / v_e + k_v * delta_v_y
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
    a = (thrust - drag) / m
    dv = a * dt
    return dv


def velocity(v, angle, dv, delta_t):
    v = v + dv
    v_x = v * cos(angle * pi / 180)
    v_y = v * sin(angle * pi / 180) - g * delta_t
    print(v_x, v_y)
    v_new = (v_x ** 2 + v_y ** 2) ** 0.5
    angle_new = tan(v_y / v_x) * 180 / pi
    return v_x, v_y, v_new, angle_new


def calc_position(x, y, v_x, v_y, delta_t):
    x = x + v_x * delta_t
    y = y + v_y * delta_t
    return x, y
