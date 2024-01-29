import numpy as np
import pytest as pt

from EulerChebA2 import EulerCheb_method


# Function
def function(x):
    return np.exp(-x)+np.cos(x+1.0)-1.0

# First derivative function
def derivative(x):
    return -1.0*np.exp(-x)-np.sin(x+1.0)

# Second derivative function
def dderivative(x):
    return np.exp(-x)-np.cos(x+1.0)

class TestEulerCheb:
    # Call Euler-Chebyshev function
    solution, record, flag = EulerCheb_method(function, derivative, dderivative, 1.0, 10, 1e-14, 1e-8)

    def test_convergence(self):
        assert self.flag == True

    def test_answer(self):
        assert self.solution == pt.approx(0.30488313307)

    def test_error(self):
        assert self.record[-1,2] < 1e-13

    def test_residual(self):
        assert self.record[-1,3] < 1e-4

    def test_iterations(self):
        assert (np.shape(self.record)[0]) <= 5
