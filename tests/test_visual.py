import pytest
#from dataviztool import dataviztool
import dataviztool

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pyvista as pv
import os
import random
import time


def test_ifworks():

    assert 2 == 2

def test_action_without_fixtures():

    thing = 2+2
    assert thing == 4

def test_if_watcher():

    sc = dataviztool.Watcher(Path("test_folder"))
    assert sc

def test_if_plotter():

    explotter = dataviztool.Displayer(automake_plotter=False)
    assert explotter

def test_more_plots():

    explotter = dataviztool.Displayer(automake_plotter=False)
    assert 1 == 1

def test_folder_name():

    mypath = Path("test_folder1")
    assert mypath == Path("test_folder1")

def test_y_coord():
    explotter = dataviztool.Displayer(automake_plotter=False)
    explotter.set_y_coord("myycoord")
    assert explotter.y_coord == "myycoord"

def test_y_coord2():
    explotter = dataviztool.Displayer(automake_plotter=False)
    explotter.set_y_coord("myycoord")
    assert type(explotter.y_coord) == str
