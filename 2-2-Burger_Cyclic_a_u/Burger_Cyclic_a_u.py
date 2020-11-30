import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
os.system('mkdir pic')

d2 = 0.1
v = 0.1
dx = dy = 0.1
span_x = 10.0
span_y = 10.0
dt = d2*dx*dx/v
print("dt: ", dt)

end_time = 100.0
print("Total Time Intervals: ", end_time/dt)

x = np.arange(0.0, span_x+dx, dx)
y = np.arange(0.0, span_y+dy, dy)
X, Y = np.meshgrid(x,y)

U = np.zeros((y.shape[0],x.shape[0]))
U[20:40,20:40] = 1.0 # Initial Condition

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, U, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('U')
ax.set_zlim([-0.1,1.1])
plt.title('Initial Condition')
plt.savefig('./pic/init.png')
plt.clf()
plt.cla()

n = 0
for it in tqdm(np.arange(0.0,end_time + dt, dt)):
    # 3D image construction
    if n%100==0:
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, U, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('U')
        ax.set_zlim([-0.1,1.1])
        plt.title(it)
        plt.savefig('./pic/%04d.png'%(n/100))
        plt.clf()
        plt.cla()
    n += 1
    U = U + d2*(np.roll(U,-1,axis=1)+np.roll(U,1,axis=1)+np.roll(U,-1,axis=0)+np.roll(U,1,axis=0)-4.0*U) - U*dt/dx*(2.0*U-np.roll(U,1,axis=0)-np.roll(U,1,axis=1))

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, U, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('U')
ax.set_zlim([-0.1,1.1])
plt.title('Final Condition')
plt.savefig('./pic/final.png')
plt.clf()
plt.cla()
