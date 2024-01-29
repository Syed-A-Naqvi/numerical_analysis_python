import numpy as np
import pytest as pt

from bisectionA2 import bisection_method


# Function
def function(x):
    return np.exp(-x)+np.cos(x+1)-1


class Testbisection:
    # Call Halley function
    solution, record, flag = bisection_method(function, 0, 1, 1000, 1e-12, 1e-8)

    def test_convergence(self):
        assert self.flag == True

    def test_answer(self):
        assert self.solution == pt.approx(0.30488313307)

    def test_error(self):
        assert self.record[-1,2] < 1e-12

    def test_residual(self):
        assert self.record[-1,3] < 1e-8

    def test_iterations(self):
        assert (np.shape(self.record)[0]) <= 1000
