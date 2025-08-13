import pytest
#from dataviztool import dataviztool
import dataviztool


explotter = dataviztool.Displayer(automake_plotter=False)

class TestSetCSVCoords():
    explotter = dataviztool.Displayer(automake_plotter=False)

    #explotter.set_csv_coords("myxcoord", "myycoord", "myzcoord", "myfieldcoord")

    def test_set_csv_coords_x(self):
        explotter.display_opts.set_csv_coords("myxcoord", "myycoord", "myzcoord", "myfieldcoord")
        assert explotter.display_opts.x_coord == "myxcoord"

    def test_set_csv_coords_y(self):
        assert explotter.display_opts.y_coord == "myycoord"

    def test_set_csv_coords_z(self):
        assert explotter.display_opts.z_coord == "myzcoord"

@pytest.mark.parametrize(
    "input_coord, expected_result",
    [
        ("myxcoord", "myxcoord"),
        ("anxcoordinate", "anxcoordinate"),
    ],
)
def test_set_x_coord(input_coord, expected_result):
    explotter.display_opts.set_x_coord(input_coord)
    assert explotter.display_opts.x_coord == expected_result

def test_x_coord_type():
    explotter.display_opts.set_x_coord("myxcoord")
    assert type(explotter.display_opts.x_coord) == str

def test_set_y_coord():
    explotter.display_opts.set_y_coord("myycoord")
    assert explotter.display_opts.y_coord == "myycoord"

def test_y_coord_type():
    explotter.display_opts.set_y_coord("myycoord")
    assert type(explotter.display_opts.y_coord) == str

def test_set_z_coord():
    explotter.display_opts.set_z_coord("myzcoord")
    assert explotter.display_opts.z_coord == "myzcoord"

def test_z_coord_type():
    explotter.display_opts.set_z_coord("myzcoord")
    assert type(explotter.display_opts.z_coord) == str

class TestCLimOptions():
    explotter = dataviztool.Displayer(automake_plotter=False)

    def test_set_clim_option(self):
        explotter.display_opts.set_clim_option(clim_option="contained", clim_min = 0, clim_max = 1, quan_min = .05, quan_max = .95)
        assert explotter.display_opts.clim_option == "contained"

    def test_set_quan_min(self):
        assert explotter.display_opts.quan_min == .05

    def test_set_quan_max(self):
        assert explotter.display_opts.quan_max == .95

    def test_set_clim_min_max(self):
        assert explotter.display_opts.clim == [0, 1]

def test_set_zoom_level():
    explotter.display_opts.set_zoom_level(1)
    assert explotter.display_opts.zoom_level == 1

def test_zoom_level_type():
    explotter.display_opts.set_zoom_level(1)
    assert type(explotter.display_opts.zoom_level) == float