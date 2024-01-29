import numpy as np
import pytest as pt

from NewtonRaphsonA2 import NewtonRaphson_method


# Function
def function(x):
    return np.exp(-x)+np.cos(x+1.0)-1.0

# First derivative function
def derivative(x):
    return -1.0*np.exp(-x)-np.sin(x+1.0) 


class TestNewtonRaphson:
    # Call Newton-Raphson function
    solution, record, flag = NewtonRaphson_method(function, derivative, 1.0, 10, 1e-12, 1e-8)

    def test_convergence(self):
        assert self.flag == True

    def test_answer(self):
        assert self.solution == pt.approx(0.30488313307)

    def test_error(self):
        assert self.record[-1,2] < 1e-12

    def test_residual(self):
        assert self.record[-1,3] < 1e-5

    def test_iterations(self):
        assert (np.shape(self.record)[0]) <= 5
