import numpy as np

angulo = float(input('digite um angulo em graus: '))

radAngulo = np.deg2rad(angulo)

print (np.sin(radAngulo))
print (np.cos(radAngulo))
print (np.tan(radAngulo))
