import numpy as np
#Metodo para resolver ecuaciones diferenciales
def rungek4(fun, t, z0):
    nt = len(t)
    nz = len(z0)
    h = t[1]-t[0]
    z = np.zeros((nt, nz))
    z[0] = z0

    for i in range(1, nt):
        m1 = fun(z[i-1])
        m2 = fun(z[i-1]+h*m1/2)
        m3 = fun(z[i-1]+h*m2/2)
        m4 = fun(z[i-1]+h*m3)
        z[i] = z[i-1]+h*(m1+2*m2+2*m3+m4)/6
    return z
