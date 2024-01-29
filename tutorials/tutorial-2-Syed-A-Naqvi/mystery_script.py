#Collaborators: Arham Naqvi, Kevin Rodriguez, Mansi Patel, Samir Rahman, Fareeha Malik

# A mystery script. In tutorial 2 you will be challenged to find out what it does and what you can learn from it.

import numpy as np
from NewtonRaphsonIteration import NewtonRaphson
import matplotlib.pyplot as plt

#these parameters correspond to the roots of the function f(x)
r1 = 0.2
r2 = 0.5
r3 = 0.9

# cubic function
def f(x):
    return (x-r1)*(x-r2)*(x-r3)

# derivative of the cubic function
def df(x):
    return (x-r2)*(x-r3)+(x-r1)*(x-r3)+(x-r1)*(x-r2)

# amount of initial x values to test for convergence
N = 1000

#left bound of the interval in which there are zeros
l = 0.0
#right bound of interval in which there are zeros
r = 1.0

#creating a list of evenly spaced initial x0 values from 0 to 1000
x0 = np.linspace(l,r,N)

#maximum allowed iterations for newton raphson
kMax = 10
#error tolerances for convergence
epsx = 1e-6
epsf = 1e-6

#this code is just creating the visual representation of convergence along the interval [0,1]
fig_width = 6.0
fig_height = 1.0
w = 72.0*fig_width/float(N)
fig = plt.figure(figsize=[fig_width,fig_height])
plt.xlim(l,r)
plt.ylim(0,1)
plt.xticks([])
plt.yticks([])


#this loop is going to test each of the 1000 evenly spaced values
for k in range(N):
    x,err,res,conv,iterations = NewtonRaphson(f,df,x0[k],kMax,epsx,epsf)
    #if there is no convergence create a black line
    if conv == 0:
        c = "k"
    #if there is convergence we will determine to which root the algorithm converges
    else:
        #if the algorithm converges to r1 then create a red line
        if abs(x-r1) < 10*epsx:
            c = 'r'
        else:
            #if the algorithm converges to r2 then create a green line
            if abs(x-r2) < 10*epsx:
                c = 'g'
            else:
                #if the algorithm converges to r3 then create a blue line
                if abs(x-r3) < 10*epsx:
                    c = 'b'

    #plotting the visual representation
    plt.plot([x0[k],x0[k]],[0,1],color=c,linewidth=w)

plt.show()

'''
For part f of exercise A my group used an "a" value of 5, upper and lower bounds of "a" and "1" respectively in the case of both
bisection and secant methods and an x0 value of 3 for the newton-raphson method.
We have found that the convergence rate of the bisection method is linear while the convergence rates for the secant and
newton-raphson methods are quadratic as evident by the overlapping semilog plot posted below. We can see clearly that the
newton-raphson method converges the quickest with the least amount of iterations being required to arrive at the smallest epsilon_x
values out of the other three methods. While the secant method has the same type of convergence as the newton-raphson method(quadratic)
it requires more iterations to converge. This is because each iteration of the secant method computes the x value for the root of the
SECANT line between two previous x values which is not as accurate a representaiton of function behaviour as the true tangent line at
a given x value. We believe that the newton-raphson method is also the most efficient as it requires the least amount of elementary
operations out of the three methods with the bisection method requiring the most.

As for the mystery script, it creates a list of 1000(N) equally spaced x values in the interval [l,r]. It then preforms the
newtown-raphson algorithm with a maximum allowed number of iterations(kmax) = 10 taking each of those 1000 x-values in the list
as initial values(guesses) upon which to preform the algorithm. The function used in the mystery code is a cubic polynomial
with roots(r1, r2, r3) and if the interval [l,r] is such that the roots fall within them, then the algorithm may converge to any of
the three roots or not converge at all depending on the initial x-value taken from the list. Now depending upon which root the
algorithm converges to, a line of a certain color is drawn: red for r1, green for r2, blue for r3 and black in the case there is no
convergence at all. We can conclude that the newton-raphson method is a powerful and efficient algorithm for determining the roots of
a function. With initial guesses that are relatively close to the true roots, the algorithm can utilize tangents that are accurate
representations of function behaviour near the roots allowing for quick convergence. There is a danger of no convergence at all in
the case that an x-value close to or equal to a minimum or maximum of the polynomial is chosen since that would result in a near
horizontal tanget which would produce a root far away from the function roots.
'''