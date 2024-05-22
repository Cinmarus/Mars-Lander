def marsinit():
    with open('marsatm.txt', 'r') as file:
        lines_init = file.readlines()
        lines_filtered = filterlines(lines_init)
        data_dict = {}
        for line in lines_filtered:
            line_split = line.split()
            key = float(line_split[0])
            values = tuple(map(float, line_split[1:4]))
            data_dict[key] = values
        return data_dict


def filterlines(lines):
    return [line for line in lines if line[0] != '*']


def mars_atm(h_m, data):
    h = h_m / 1000
    R = 191.84
    h_keys = list(data.keys())
    n = 0
    for i in range(len(h_keys)):
        if h_keys[i] > h:
            n = i
            break
    h1 = h_keys[n - 1]
    h2 = h_keys[n]
    t, rho, c = interpolate(data, h1, h2, h)
    p = rho * R * t
    return p, rho, t, c


def interpolate(data, h1, h2, h):
    t1, rho1, c1 = data[h1]
    t2, rho2, c2 = data[h2]
    t = t1 + (t2 - t1) / (h2 - h1) * (h - h1)
    rho = rho1 + (rho2 - rho1) / (h2 - h1) * (h - h1)
    c = c1 + (c2 - c1) / (h2 - h1) * (h - h1)
    return t, rho, c
