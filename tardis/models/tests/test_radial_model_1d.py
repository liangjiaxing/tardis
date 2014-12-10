import pytest

import numpy as np

import numpy.testing as nptesting

from astropy import units as u

from tardis.models.model1d import Radial1D


def test_simple_radial_model1d_1():
    radius = np.arange(1000, 11000, 1000) * u.km
    density = np.linspace(1e8, 1e9, 10) * u.Msun / u.AU**3
    test_model = Radial1D(radius, density, None, None)

    assert test_model.radius.unit == u.cm
    assert test_model.density.unit == u.g / u.cm**3

    nptesting.assert_allclose(test_model.volume[0],
                              4.1887902047863903e+24 * u.cm**3)

    nptesting.assert_allclose(test_model.mass[0],  2.488679615529453e+26 * u.g)
