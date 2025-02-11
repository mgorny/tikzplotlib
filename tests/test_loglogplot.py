import matplotlib.pyplot as plt
import numpy as np


def plot():
    fig = plt.figure()
    x = np.logspace(0, 6, num=5)
    plt.loglog(x, x ** 2, lw=2.1)
    return fig


def test():
    from .helpers import assert_equality

    assert_equality(plot, __file__[:-3] + "_reference.tex")
