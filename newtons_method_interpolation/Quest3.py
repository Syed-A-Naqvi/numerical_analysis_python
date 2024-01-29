# script for Question 3 of Assignment #4
#   for polynomial interpolation using the Newton polynomial basis

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

from NewtonPolyBuildA4 import NewtonPolyBuild
from NewtonPolyEvalA4 import NewtonPolyEval


#  enter data points
xs = np.array([0,1.0,2.0,3.0,4.0,5.0])
ys = np.array([1.00,0.90,-0.21,-0.65,0.68,0.11])

#  Call NewtonPolyBuild for contructing matrix M
M = NewtonPolyBuild(xs)

#  Solve system of equations to find coefficients of interpolant
a = scipy.linalg.solve(M,ys)

#  Call NewtonPolyEval to get values for plotting
xx = np.linspace(0,5,1000,endpoint=True)
yy = NewtonPolyEval(a,xs,xx)

#  plot data and interpolant
#   don't forget to label plot appropriately
plt.plot(xs, ys, 'ro', label='data points')
plt.plot(xx, yy, '-g', label='Interpolant')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Interpolation for Set of Interpolating Nodes')
plt.legend()
plt.show()