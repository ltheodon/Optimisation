import fun
import random
import matplotlib.pyplot as plt
import numpy as np

# Fonction gradient
def grad(x,dx,f):
	return (f(x+dx) - f(x-dx))/(2*dx)

# Definition des parametres et initialisation
dx = 1.e-2
x = [random.randint(-7, 7)]
gradx = [grad(x[-1],dx,fun.f)]
sigma = 2
nmax = 200
n = 0
budget = 5
eps = 1.e-5

# Mise en oeuvre de l'algorithme
while abs(gradx[-1]) > eps and n < nmax:
	n += 1
	xnext = x[-1]
	for i in range(budget):
		xnew = x[-1] + sigma*np.random.normal(0, 1, 1)
		if fun.f(xnew) < fun.f(xnext):
			xnext = xnew
	x.append(xnext)
	gradx.append(grad(x[-1],dx,fun.f))


# Affichage des resultats
t = np.arange(-10., 10., 0.1)
plt.subplot(121)
plt.plot(t,list(map(fun.f,t)), 'b-', label="f(x)")
plt.plot(x,list(map(fun.f,x)), 'rx', label="x_n")
plt.legend()
plt.subplot(122)
plt.plot(range(n+1),list(map(abs,gradx)), 'y-', label="Module du gradient")
plt.plot(range(n+1),[eps for i in range(n+1)], 'r--', label="eps")
plt.legend()
plt.suptitle('Progression de la convergence')
plt.show()