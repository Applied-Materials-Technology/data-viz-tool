import pytest
#from dataviztool import dataviztool
import dataviztool


explotter = dataviztool.Displayer(automake_plotter=False)

def test_y_coord():
    explotter.set_y_coord("myycoord")
    assert explotter.y_coord == "myycoord"

def test_y_coord_type():
    explotter.set_y_coord("myycoord")
    assert type(explotter.y_coord) == str