import numpy as np
import pytest as pt

from NewtonRaphsonA2 import NewtonRaphson_method


# Function
def function(x):
    return 4.0*x**4 - 8.0*x**3 + 7.0*x**2 - 3.0*x + 1/2

# First derivative function
def derivative(x):
    return 16.0*x**3 - 24.0*x**2 + 14.0*x - 3.0


class TestNewtonRaphson:
    # Call NewtonRaphson function
    solution, record, flag = NewtonRaphson_method(function, derivative, 1.0, 30, 1e-8, 1e-8)

    def test_convergence(self):
        assert self.flag == True

    def test_answer(self):
        assert self.solution == pt.approx(0.5000000)

    def test_error(self):
        assert self.record[-1,2] < 1e-8

    def test_residual(self):
        assert self.record[-1,3] < 1e-4

    def test_iterations(self):
        assert (np.shape(self.record)[0]) <= 47
