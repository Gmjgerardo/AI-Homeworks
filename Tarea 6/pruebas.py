import numpy as np
import matplotlib.pyplot as plt

Listanumpys = []

for i in range(5):
    Listanumpys.append(np.array([1,2,3,4,5]))

suma = np.array([0,0,0,0,0])

completon = Listanumpys[0] + Listanumpys[1] + Listanumpys[2] + Listanumpys[3] + Listanumpys[4]
otro = Listanumpys[0] + Listanumpys[1:]
sumer = np.add.reduce(Listanumpys)

xpoints = np.array([0, 100, 200, 300, 400])
ypoints = np.array([25, 20, 15, 10, 5])

print(np.array(list(range(0, 1000 + 1, 100))))

for ejecucion in Listanumpys:
    suma = suma + ejecucion

print(suma)
print(completon)
print(otro)

# Creamos una figura
plt.figure(1)
fig, ax = plt.subplots()
fig.set_label('2')

ax.plot(xpoints, ypoints,label='Men')
ax.plot(xpoints, np.array([45, 40, 35, 30, 25]), label='Women')
ax.legend()
""" plt.plot(xpoints, ypoints, label='Holo')
plt.plot(xpoints, np.array([45, 40, 35, 30, 25]), label='REimpo')
plt.plot(xpoints, np.array([15, 10, 5, 0, -5]), label='Deic') """
plt.show()
