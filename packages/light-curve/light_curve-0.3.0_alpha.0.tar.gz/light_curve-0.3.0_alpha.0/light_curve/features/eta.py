import numpy as np

from ._base import BaseFeature


class Eta(BaseFeature):
    def __call__(self, t, m, sigma=None, sorted=None, fill_value=None):
        n = len(m)
        m_std = np.var(m, ddof=1)
        m_sum = np.sum((m[1:] - m[:-1]) ** 2)
        return m_sum / ((n - 1) * m_std)


__all__ = ("Eta",)
