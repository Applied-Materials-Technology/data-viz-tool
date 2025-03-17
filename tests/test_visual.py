import pytest
from dataviztool import dataviztool

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
    sc = dataviztool.Watcher()

    thing = sc.do_i_test(3)
    assert thing == 4

