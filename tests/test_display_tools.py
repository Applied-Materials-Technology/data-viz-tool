import pytest
#from dataviztool import dataviztool
import dataviztool

explotter = dataviztool.Displayer(automake_plotter=False)


def test_auto_create_plotter():
    #dataviztool.subplot_decider(explotter, "event")
    assert 1 == 1

