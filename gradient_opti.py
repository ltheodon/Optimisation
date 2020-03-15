import fun
import random
import matplotlib.pyplot as plt
import numpy as np

def grad(x,dx,f):
	return (f(x+dx) - f(x-dx))/(2*dx)


# Definition des parametres et initialisation
x = [random.randint(-4, 4)]
dx = 1.e-2
gradx = [grad(x[-1],dx,fun.f)]
eps = 1.e-5
step = 1.e-1
nmax = 100
n = 0

# Mise en oeuvre de l'algorithme
while abs(gradx[-1]) > eps and n < nmax:
	n += 1
	if gradx[-1] < 0:
		istep = 1
		while grad(x[-1] + istep * step,dx,fun.f) < 0:
			istep += 1
		x.append(x[-1] + istep * step)
		gradx.append(grad(x[-1],dx,fun.f))
	else:
		istep = 1
		while grad(x[-1] - istep * step,dx,fun.f) > 0:
			istep += 1
		x.append(x[-1] - istep * step)
		gradx.append(grad(x[-1],dx,fun.f))
 

# Affichage des resultats
t = np.arange(-5., 5., 0.1)
dt = [grad(p,dx,fun.f) for p in t]
plt.subplot(121)
plt.plot(t,list(map(fun.f,t)), 'b-', label="f(x)")
plt.plot(x,list(map(fun.f,x)), 'rx', label="x_n")
plt.legend()
#plt.plot(t,dt, 'g--')
plt.subplot(122)
plt.plot(range(n+1),list(map(abs,gradx)), 'y-', label="Module du gradient")
plt.plot(range(n+1),[step for i in range(n+1)], 'r--', label="step")
plt.legend()
plt.suptitle('Progression de la convergence')
plt.show()