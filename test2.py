def poweration(a,b):
    return a**b

def SphereVolume(a, type='radius'):
    if type == 'radius':
        a = a
    elif type == 'diameter':
        a = a/2
    return (4/3)*poweration(a,3)
