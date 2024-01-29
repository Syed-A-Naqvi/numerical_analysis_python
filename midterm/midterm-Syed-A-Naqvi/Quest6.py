#  Starter code for Question 6 of Midterm Test


#  import functions and modules you will use
import numpy as np
import numpy.linalg as npln
import scipy as sc
import scipy.linalg as scln

#  insert code for computing Maximal Relative Error 
A = np.array([[1.0,  0.0,  2.0],
              [ 1.0,  0.0, 1.9 ],
              [ 1.0, 3.0, 11.0 ]])

b = np.array([1.0, 1.0, 4.0])

x_star = np.array([1.000023, 0.999971, 0.000019]) #npln.solve(A,b)

res = npln.norm(b - A@x_star, 2)
rel_res = npln.norm(b - A@x_star, 2)/npln.norm(b, 2)
max_rel_err = npln.cond(A) * rel_res



#   write out solution 
print("Maximal Relative Error = ", max_rel_err)
