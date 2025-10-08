import pytest
import dataviztool

def test_auto_create_plotter():

    explotter = dataviztool.Displayer(automake_plotter=True, watch_path="test_inputloc")
    assert explotter.p is not None

def test_no_auto_create():

    explotter = dataviztool.Displayer(automake_plotter=False)
    assert explotter.p == None

def test_manual_create_plotter_size():

    explotter = dataviztool.Displayer(automake_plotter=False)
    explotter.create_plotter(1,2)
    assert explotter.p.shape == (1,2)


subplot_assignment = [("left", [0,0]),
            ("right", [0,1]),]

@pytest.mark.parametrize("x ,expected", subplot_assignment)
def test_manual_subplot_assign(x, expected):

    explotter = dataviztool.Displayer(automake_plotter=False, watch_path="test_inputloc")
    explotter.create_plotter(1,2)
    explotter.assign_subplot(0,0,"Experimental", "left")
    explotter.assign_subplot(0,1,"Simulation", "right")
    assert explotter._subplot_dict[x] == expected