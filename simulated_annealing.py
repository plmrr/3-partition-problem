import random
from math import e


def x_new(s_temp):
    x = []
    for _ in range(m):
        temp_list = random.sample(s_temp, 3)
        x.append(temp_list)
        for temp in temp_list:
            s_temp.remove(temp)
    return x


def err(x):
    return sum(abs(sum(part) - T) for part in x)


def annealing(temp, lam, epochs):
    s_temp = s.copy()
    x = x_new(s_temp)
    err_x = err(x)

    for _ in range(epochs):
        s_temp = s.copy()
        x_prim = x_new(s_temp)
        err_x_prim = err(x_prim)

        if err_x_prim < err_x or random.uniform(0, 1) < e**((err_x-err_x_prim)/temp):
            x = x_prim
            err_x = err_x_prim

        temp = lam * temp

    return x


s = [55, 17, 33, 44, 23, 15, 54, 31, 7, 53, 40, 28]
mT = sum(s)
m = (len(s)/3)
T = int(mT/m)

if m % 1 == 0:
    m = int(m)
    result = annealing(100, 0.9, 30000)  # input: T0, lambda, epochs
    print(f'Result of the division: {result}')
else:
    print('The number of figures is not divisible by 3, division is impossible.')
