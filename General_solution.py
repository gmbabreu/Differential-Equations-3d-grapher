import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from numpy.linalg import eig



def Y(t, w, v):
    """
    Returns the general solution of the given eigenvalues and vector of a system at a certain time
    Constants are all set to 1
    """
    return (v[0]*(np.e**(w[0]*t))) +  (v[1]*(np.e**(w[1]*t))) +  (v[2]*(np.e**(w[2]*t)))

def sol(a):
    """
    Plots the system for a given matrix of a linear system
    """
    w,v=eig(a)

    print('E-value:', w)
    print('E-vector', v)

    t = np.linspace(0, 50, 1000)


    fig = plt.figure(figsize = (8,8))
    plt.plot(t, Y(t, w, v[:,0]), label = "x(t)")
    plt.plot(t, Y(t, w, v[:,1]), label = "y(t)")
    plt.plot(t, Y(t, w, v[:,2]), label = "z(t)")
    plt.legend()
    plt.show()



a = np.array([[0, 0.1, 0], 
              [0, 0, 0.2],
              [0.4, 0, 0]])

sol(a)

a = np.array([[-2, 2, 4], 
              [0, -3, 5],
              [0, 1, -4]])

sol(a)
