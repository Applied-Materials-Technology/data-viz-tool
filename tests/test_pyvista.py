import pyvista as pv
from dataclasses import dataclass
import pytest
import numpy as np
import dataviztool as dv

dv.pv.OFF_SCREEN = True
"""
def test_succeeds(verify_image_cache):
    pl = dv.pv.Plotter()
    pl.add_mesh(dv.pv.Sphere(), show_edges=True)
    pl.show()

myplotter = dv.Displayer(automake_plotter=False)"""

def test_succeeds2():
    assert 1 == 1

