#  Starter code for Question 7 of Midterm Test


#  import functions and modules you will use
import numpy as np
import numpy.linalg as npln

#  insert code for computing the solution of the linear system 
A = np.array([[1.2,  0.2,  -0.9],
              [ 1.1,  -1.2, 0.3 ],
              [0.2, 2.1, -1.1 ]])

b = np.array([0.1, 0.3, -1.2])

x_star = npln.solve(A,b) #npln.solve(A,b)


#   write out solution 
print("Solution vector x_starr = ", x_star)
print("First component of approximate solution = ", x_star[0])

