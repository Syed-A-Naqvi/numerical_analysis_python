#  Starter code for Question 6 of Final Exam Part 2



# include necessary code



# make the plot

# polynomial interpolation

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from scipy.interpolate import BarycentricInterpolator

def f(x):
    return 1/(1+(np.cos(2*x))**2)

x = np.array([0.0,0.2,0.4,0.6,0.8,1.0])
y = np.array([f(0.0),f(0.2),f(0.4),f(0.6),f(0.8),f(1.0)])

xx = np.linspace(0,1,num=100,endpoint=True)
yy = f(xx)                        #  evaluate the interpolate at values from xx

#  use Vandermonde matrix to find interpolant
V = np.vander(x)
a_coeff = scipy.linalg.solve(V,y)    #  gives coefficients of the polynomial interpolant

# evaluate the interpolant at values from xx;
#   note the order in which a_ceoff stores coefficients when we use np.vander to get Vandermonde matrix
yy2 = a_coeff[0]*xx*xx*xx*xx*xx + a_coeff[1]*xx*xx*xx*xx + a_coeff[2]*xx*xx*xx + a_coeff[3]*xx*xx + a_coeff[4]*xx + a_coeff[5]

#  the two polynomial interpolants (i.e yy and yy2) are the same (because the interpolant is unique)
plt.plot(x,y,'ro',xx,yy,'-b',xx,yy2,'-m')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Points(red), Interpolant(magenta) and Original Function(blue)')
plt.show()