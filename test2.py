import numpy as np

def poweration(a,b):
    return a**b

def SphereVolume(a, type='radius'):
    if type == 'radius':
        pass
    elif type == 'diameter':
        a /= 2
    return (4/3)*np.pi*poweration(a,3)
