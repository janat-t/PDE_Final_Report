import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from tqdm import tqdm
import os
os.system('mkdir pic')

def plot(x, y, t, path):
	fig, ax = plt.subplots()
	ax.set_xlim(0, 100)
	ax.set_ylim(-0.25, 1.50)
	ax.xaxis.set_major_locator(MultipleLocator(20))
	ax.yaxis.set_major_locator(MultipleLocator(0.25))
	ax.grid(which='major', color='#CCCCCC', linestyle='--')
	ax.plot(x, y, '-k')
	ax.set_xlabel('x')
	ax.set_ylabel('f')
	plt.title('t='+t)
	plt.savefig(path)
	plt.close()

C = 0.1
u = 1.0
dx = 1.0
span_x = 100.0
dt = C*dx/u
print("dt: ", dt)

end_time = 600.0
print("Total Time Intervals: ", end_time/dt)

x = np.arange(0.0, span_x+dx, dx)
f = np.zeros_like(x)
f[40:61] = 1.0

plot(x,f,'Initial Condition', 'init.png')

n = 0
for i in tqdm(np.arange(0.0,end_time+dt, dt)):
	if n%10==0 and i <= 100.0:
		plot(x,f, '%.2f'%(i),'./pic/%04.0f.png'%(i) )
	if int(i*100)/100==10:
		plot(x,f,'10.0','10.png')
	if int(i*100)/100==200:
		plot(x,f,'200.0','200.png')
	if int(i*100)/100==400:
		plot(x,f,'400.0','400.png')
	if int(i*100)/100==600:
		plot(x,f,'600.0','600.png')
	n+=1
	c = f
	b = 0.5/dx*(np.roll(f,-1,axis=0)-np.roll(f,1,axis=0))
	a = 0.5/dx/dx*(np.roll(f,-1,axis=0)+np.roll(f,1,axis=0)-2.0*f)
	f = a*(u*dt)**2-b*(u*dt)+c

plot(x,f,'Final Condition', 'final.png')



