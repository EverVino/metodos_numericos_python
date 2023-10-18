import numpy as np
import reactores
import rk4

import matplotlib.pyplot as plt
# Realizando modificaciones desde un celular
t = np.linspace(0, 80, 100)
C0 = np.array([0, 0, 0, 0])

C = rk4.rungek4(reactores.edo_reactores,t,C0)

fig, ax = plt.subplots()

ax.plot(t, C[:,0] , color = "blue")
ax.plot(t, C[:,1] , color = "red")
ax.plot(t, C[:,2] , color = "orange")
ax.plot(t, C[:,3] , color = "green")

ax.set_title("Concentración vs tiempo")
ax.set_xlabel("t[min]")
ax.set_ylabel("C[mol/L]")
ax.grid()
plt.show()
