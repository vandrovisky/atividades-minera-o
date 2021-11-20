import numpy as np

x = [1, 2, 3]
y = [4, 5, 6]

escalar = np.dot(x,y)
vetorial = np.cross(x,y)

print('produto escalar: ', escalar)
print('produto vetorial: ', vetorial)