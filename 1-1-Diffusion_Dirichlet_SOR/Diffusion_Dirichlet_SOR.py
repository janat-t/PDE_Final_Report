import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm, trange
import os
os.system('mkdir pic')

dx = dy = 1.0
span_x = 100.0
span_y = 100.0
g = 9.81
rho = 1.0
Tension = 1000.0
omega = 1.7
n = 1000
print("Total Iteration: ", n)

x = np.arange(0.0, span_x+dx, dx)
y = np.arange(0.0, span_y+dy, dy)
X, Y = np.meshgrid(x,y)

## Dirichlet Boundary Condition

T = np.zeros((y.shape[0],x.shape[0]))
# Dirichlet Boundary Condition
T[:,-1] = T [:,0] = T[0,:] = T[-1,:] = 0.0

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, T, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')
ax.set_zlim([-10.0,1.0])
plt.title('Initial Condition')
plt.savefig('./pic/init.png')
plt.clf()
plt.cla()


for it in trange(n):

    # 3D image construction
    if it%10==0:
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, T, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('T')
        ax.set_zlim([-10.0,1.0])
        plt.title('omega = %.2f\nit = %d'%(omega, it))
        plt.savefig('./pic/%04d.png'%(it/10))
        plt.clf()
        plt.cla()
    for i in range(1,T.shape[0]-1):
        for j in range(1,T.shape[1]-1):
            R = 0.25*(T[i+1][j]+T[i-1][j]+T[i][j+1]+T[i][j-1]-dx*dy*g*rho/Tension)
            T[i][j] = (1-omega)*T[i][j]+omega*R


ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, T, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')
ax.set_zlim([-10.0,1.0])
plt.title('Final Condition')
plt.savefig('./pic/final.png')
plt.clf()
plt.cla()
