import pytest
#from dataviztool import dataviztool
import dataviztool


explotter = dataviztool.Displayer(automake_plotter=False)

class TestSetCSVCoords():
    explotter = dataviztool.Displayer(automake_plotter=False)

    #explotter.set_csv_coords("myxcoord", "myycoord", "myzcoord", "myfieldcoord")

    def test_set_csv_coords_x(self):
        explotter.set_csv_coords("myxcoord", "myycoord", "myzcoord", "myfieldcoord")
        assert explotter.x_coord == "myxcoord"

    def test_set_csv_coords_y(self):
        assert explotter.y_coord == "myycoord"

    def test_set_csv_coords_z(self):
        assert explotter.z_coord == "myzcoord"

@pytest.mark.parametrize(
    "input_coord, expected_result",
    [
        ("myxcoord", "myxcoord"),
        ("anxcoordinate", "anxcoordinate"),
    ],
)
def test_set_x_coord(input_coord, expected_result):
    explotter.set_x_coord(input_coord)
    assert explotter.x_coord == expected_result

def test_x_coord_type():
    explotter.set_x_coord("myxcoord")
    assert type(explotter.x_coord) == str

def test_set_y_coord():
    explotter.set_y_coord("myycoord")
    assert explotter.y_coord == "myycoord"

def test_y_coord_type():
    explotter.set_y_coord("myycoord")
    assert type(explotter.y_coord) == str

def test_set_z_coord():
    explotter.set_z_coord("myzcoord")
    assert explotter.z_coord == "myzcoord"

def test_z_coord_type():
    explotter.set_z_coord("myzcoord")
    assert type(explotter.z_coord) == str

class TestCLimOptions():
    explotter = dataviztool.Displayer(automake_plotter=False)

    def test_set_clim_option(self):
        explotter.set_clim_option(clim_option="contained", clim_min = 0, clim_max = 1, quan_min = .05, quan_max = .95)
        assert explotter.clim_option == "contained"

    def test_set_quan_min(self):
        assert explotter.quan_min == .05

    def test_set_quan_max(self):
        assert explotter.quan_max == .95

    def test_set_clim_min_max(self):
        assert explotter.clim == [0, 1]

def test_set_zoom_level():
    explotter.set_zoom_level(1)
    assert explotter.zoom_level == 1

def test_zoom_level_type():
    explotter.set_zoom_level(1)
    assert type(explotter.zoom_level) == float