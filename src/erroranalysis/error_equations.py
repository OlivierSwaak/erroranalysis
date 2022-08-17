import numpy as np

def erro_devide(a,da,b,db):
    x = a/b
    dx = x * np.sqrt((da/a)**2+(db/b)**2)
    return x, dx

def error_multiplicate(a,da,b,db):
    x = a*b
    dx = x * np.sqrt((da/a)**2+(db/b)**2)
    return x, dx

def error_sum(da,db):
    x = a+b
    dx = np.sqrt(da**2 + db**2)
    return x, dx

def error_difference(da,db):
    x = a-b
    dx = np.sqrt(da**2 + db**2)
    return x, dx