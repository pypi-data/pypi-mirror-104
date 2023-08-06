import numpy as np
from numpy.testing import assert_allclose

from light_curve_pure import Plateau


def test_plateau_one_outlier():
    n = 100
    rng = np.random.default_rng(0)
    t = np.linspace(0, 1, n)
    m = rng.normal(0, 1, n)
    m[0] += 10
    feature = Plateau()
    actual = feature(t, m)
    desired = 1 - 1 / n
    assert_allclose(actual, desired)


def test_plateau_step():
    n = 100
    desired = 0.9
    rng = np.random.default_rng(0)
    t = np.linspace(0, 1, n)
    m = rng.normal(0, 1, n)
    m[int(desired * n) :] += 6
    feature = Plateau()
    actual = feature(t, m)
    assert_allclose(actual, desired)


def test_plateau_linear():
    n = 100
    desired = 0.8
    n_linear = int(n * (1 - desired))
    rng = np.random.default_rng(0)
    t = np.arange(n)
    m = rng.normal(0, 1, n)
    m[:n_linear] += t[:n_linear]
    feature = Plateau()
    actual = feature(t, m)
    assert_allclose(actual, desired)
