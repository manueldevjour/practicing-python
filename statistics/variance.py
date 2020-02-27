import numpy as np
datos = np.array([
[0,1,2,3,4,5,6,7,8,9],
[2,3,2,3,4,5,6,7,6,7],
[2,3,2,3,4,5,6,7,8,9],
[2,3,2,3,2,3,2,3,2,3],
[3,4,5,4,5,6,7,7,8,8],
[1,1,1,1,1,1,1,1,1,1],
[5,5,6,6,7,7,8,8,9,9],
[1,1,2,2,3,3,4,4,5,5]
])
for dato in datos:
    print('Array: ', dato)
    print('Media: ', dato.mean())
    print('Desvi: ', np.std(dato))
    print('Varia: ', np.var(dato))
    print(' ')