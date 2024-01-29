import pytest as pt
import numpy as np
from CondNumFuncA3 import CondNumFunc

def test_CondNum():
    a = 7
    assert (CondNumFunc(a)-7.49726184) <= 1.0e-5

