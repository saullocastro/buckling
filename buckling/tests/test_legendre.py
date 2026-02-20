import numpy as np
from buckling import legendre

def test_f_boundary_conditions():
    # Test displacement functions
    # i=0 should be 1 at xi=-1 and 0 at xi=1
    assert np.isclose(legendre.f(-1, 0, 1, 0, 0, 0), 1.0)
    assert np.isclose(legendre.f(1, 0, 1, 0, 0, 0), 0.0)
    # i=2 should be 0 at xi=-1 and 1 at xi=1
    assert np.isclose(legendre.f(-1, 2, 0, 0, 1, 0), 0.0)
    assert np.isclose(legendre.f(1, 2, 0, 0, 1, 0), 1.0)

    # Test rotation-related functions (should be 0 at both ends)
    # i=1
    assert np.isclose(legendre.f(-1, 1, 0, 1, 0, 0), 0.0)
    assert np.isclose(legendre.f(1, 1, 0, 1, 0, 0), 0.0)
    # i=3
    assert np.isclose(legendre.f(-1, 3, 0, 0, 0, 1), 0.0)
    assert np.isclose(legendre.f(1, 3, 0, 0, 0, 1), 0.0)


def test_fxi_boundary_conditions():
    # Test displacement functions (derivatives should be 0 at ends)
    # i=0
    assert np.isclose(legendre.fxi(-1, 0, 1, 0, 0, 0), 0.0)
    assert np.isclose(legendre.fxi(1, 0, 1, 0, 0, 0), 0.0)
    # i=2
    assert np.isclose(legendre.fxi(-1, 2, 0, 0, 1, 0), 0.0)
    assert np.isclose(legendre.fxi(1, 2, 0, 0, 1, 0), 0.0)

    # Test rotation functions
    # i=1 should have derivative 0.5 at xi=-1 and 0 at xi=1
    assert np.isclose(legendre.fxi(-1, 1, 0, 1, 0, 0), 0.5)
    assert np.isclose(legendre.fxi(1, 1, 0, 1, 0, 0), 0.0)
    # i=3 should have derivative 0 at xi=-1 and 0.5 at xi=1
    assert np.isclose(legendre.fxi(-1, 3, 0, 0, 0, 1), 0.0)
    assert np.isclose(legendre.fxi(1, 3, 0, 0, 0, 1), 0.5)
def test_derivative_relationship():
    # Check if fxi is the derivative of f for i=4
    xi_points = np.linspace(-1, 1, 10)
    for xi in xi_points:
        # f(xi, 4, ...) = 0.125*xi**4 - 0.25*xi**2 + 0.125
        # fxi_analytical = 0.5*xi**3 - 0.5*xi
        fxi_analytical = 0.5 * xi**3 - 0.5 * xi
        assert np.isclose(legendre.fxi(xi, 4, 0, 0, 0, 0), fxi_analytical)

def test_gauss_quadrature_weights():
    for n in range(2, 41):
        _, weights = legendre.gauss_quadrature(n)
        assert np.isclose(np.sum(weights), 2.0)

def test_vecf_calls():
    # Check if vecf calls f correctly for a few values
    d1t, d1r, d2t, d2r = 1, 1, 1, 1
    xi = 0.5
    vec = legendre.vecf(5, xi, d1t, d1r, d2t, d2r)
    for i in range(5):
        assert np.isclose(vec[i], legendre.f(xi, i, d1t, d1r, d2t, d2r))

def test_vecfxi_calls():
    # Check if vecfxi calls fxi correctly for a few values
    d1t, d1r, d2t, d2r = 1, 1, 1, 1
    xi = 0.5
    vec = legendre.vecfxi(5, xi, d1t, d1r, d2t, d2r)
    for i in range(5):
        assert np.isclose(vec[i], legendre.fxi(xi, i, d1t, d1r, d2t, d2r))

def test_vecfxixi_calls():
    # Check if vecfxixi calls fxixi correctly for a few values
    d1t, d1r, d2t, d2r = 1, 1, 1, 1
    xi = 0.5
    vec = legendre.vecfxixi(5, xi, d1t, d1r, d2t, d2r)
    for i in range(5):
        assert np.isclose(vec[i], legendre.fxixi(xi, i, d1t, d1r, d2t, d2r))

