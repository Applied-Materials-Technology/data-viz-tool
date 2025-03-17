import pyvista as pv
import pytest

pv.OFF_SCREEN = True
def test_succeeds(verify_image_cache):
    pl = pv.Plotter()
    pl.add_mesh(pv.Sphere(), show_edges=True)
    pl.show()


