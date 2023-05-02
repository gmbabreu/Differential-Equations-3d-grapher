import numpy as np
import matplotlib.pyplot as plt


def phase(a):
    # Define a grid of initial conditions to plot the phase plane
    x = np.linspace(-10, 10, 5)
    y = np.linspace(-10, 10, 5)
    z = np.linspace(-10, 10, 5)

    X, Y, Z = np.meshgrid(x, y, z)
    
    dx = np.zeros_like(X)
    dy = np.zeros_like(Y)
    dz = np.zeros_like(Z)
    
    # For every point in the grid, define the slope at that point
    for i in range(len(x)):
        for j in range(len(y)):
            for k in range(len(z)):
                dx[i,j,k] = a[0,0]*X[i,j,k] + a[0,1]*Y[i,j,k] + a[0,2]*Z[i,j,k]
                dy[i,j,k] = a[1,0]*X[i,j,k] + a[1,1]*Y[i,j,k] + a[1,2]*Z[i,j,k]
                dz[i,j,k] = a[2,0]*X[i,j,k] + a[2,1]*Y[i,j,k] + a[2,2]*Z[i,j,k]

    # Create the phase plane plot
    fig = plt.figure(figsize=(10,10))
    ax = fig.gca(projection='3d')
    ax.quiver(X, Y, Z, dx, dy, dz, length=2, normalize=True)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z)")
    plt.show()


a = np.array([[0, 0.1, 0], 
              [0, 0, 0.2],
              [0.4, 0, 0]])

phase(a)

a = np.array([[-2, 2, 4], 
              [0, -3, 5],
              [0, 1, -4]])

phase(a)
