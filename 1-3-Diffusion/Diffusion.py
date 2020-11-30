import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
os.system('mkdir pic')

d = 0.251
alpha = 0.1
dx = dy = 0.1
span_x = 10.0
span_y = 10.0
dt = d*dx*dx/alpha
print("dt: ", dt)

end_time = 50.0
print("Total Time Intervals: ", end_time/dt)

x = np.arange(0.0, span_x+dx, dx)
y = np.arange(0.0, span_y+dy, dy)
X, Y = np.meshgrid(x,y)

## Dirichlet Boundary Condition

T = np.zeros((y.shape[0],x.shape[0]))
# Initial Condition
T[30:40,40:60] = 100.0
T[60:70,40:60] = 100.0


ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, T, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
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
    # 3D image construction
    if (int)(it*10)%10==0:
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, T, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('T')
        ax.set_zlim([-10.0,110.0])
        plt.title('d = %.3f\n%.2f'%(d,it))
        plt.savefig('./pic/%04d.png'%((int)(it*10)/10))
        plt.clf()
        plt.cla()
    n += 1
    T = T + d*(np.roll(T,-1,axis=1)-4.0*T+np.roll(T,1,axis=1)+np.roll(T,-1,axis=0)+np.roll(T,1,axis=0))

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, T, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')
ax.set_zlim([-10.0,110.0])
plt.title('Final Condition')
plt.savefig('./pic/final.png')
plt.clf()
plt.cla()
