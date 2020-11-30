import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
os.system('mkdir pic')

d = 0.1
alpha = 0.1
dx = dy = 0.1
span_x = 10.0
span_y = 10.0
dt = d*dx*dx/alpha
print("dt: ", dt)

end_time = 100.0
print("Total Time Intervals: ", end_time/dt)

x = np.arange(0.0, span_x+dx, dx)
y = np.arange(0.0, span_y+dy, dy)
X, Y = np.meshgrid(x,y)

## Neumann Boundary Condition

T = np.zeros((y.shape[0],x.shape[0]))
T[20:40,20:40] = 100.0 # Initial Condition

# Neumann Boundary Condition G=0.0
T[0,:] = T[2,:];
T[:,0] = T[:,2];
T[-1,:] = T[-3,:];
T[:,-1] = T[:,-3];

ax = plt.axes(projection='3d')
ax.plot_surface(X[1:-2,1:-2], Y[1:-2,1:-2], T[1:-2,1:-2], rstride=5, cstride=5, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')
ax.set_zlim([-10.0,110.0])
plt.title('Initial Condition')
plt.savefig('./pic/init.png')
plt.clf()
plt.cla()

n = 0
for it in tqdm(np.arange(0.0,end_time + dt, dt)):
    # Neumann Boundary Condition G=0.0
    T[0,:] = T[2,:];
    T[:,0] = T[:,2];
    T[-1,:] = T[-3,:];
    T[:,-1] = T[:,-3];
    
    # 3D image construction
    if n%100==0:
        ax = plt.axes(projection='3d')
        ax.plot_surface(X[1:-2,1:-2], Y[1:-2,1:-2], T[1:-2,1:-2], rstride=5, cstride=5, cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('T')
        ax.set_zlim([-10.0,110.0])
        plt.title(it)
        plt.savefig('./pic/%04d.png'%(n/100))
        plt.clf()
        plt.cla()
    n += 1
    T = T + d*(np.roll(T,-1,axis=1)+np.roll(T,1,axis=1)+np.roll(T,-1,axis=0)+np.roll(T,1,axis=0)-4.0*T)
 
# Neumann Boundary Condition G=0.0
T[0,:] = T[2,:];
T[:,0] = T[:,2];
T[-1,:] = T[-3,:];
T[:,-1] = T[:,-3];

ax = plt.axes(projection='3d')
ax.plot_surface(X[1:-2,1:-2], Y[1:-2,1:-2], T[1:-2,1:-2], rstride=5, cstride=5, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')
ax.set_zlim([-10.0,110.0])
plt.title('Final Condition')
plt.savefig('./pic/final.png')
plt.clf()
plt.cla()