import pytest as pt
import numpy as np

from GenMatVecA3 import GenMatVec
from LowTriangMatVecA3 import LowTriangMatVec

def test_execution():
    n = 500
    A = np.random.rand(n,n)           # Set up random matrix and right hand side
    x = np.random.rand(n,1)
 
    L = np.eye(n,n)+np.tril(A,-1)

    assert np.linalg.norm((np.matmul(A,x) - GenMatVec(A,x)), 2) <= 1e-6

    assert np.linalg.norm((np.matmul(L,x) - LowTriangMatVec(L,x)), 2) <= 1e-6