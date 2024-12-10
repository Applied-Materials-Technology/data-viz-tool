import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from pathlib import Path
import os

from matplotlib.colors import ListedColormap


p = pv.Plotter(shape=(1,2))

rwi = pv.RenderWindowInteractor(p)


#print(p.render_window.IsCurrent())
p2 = pv.Plotter(shape=(1,1))
renderer1 = p.renderers
#print(renderer1)
#print(renderer1._plotter)
#print(renderer1.active_renderer)
#print(dir(renderer1))
#rwi.set_render_window(p.render_window)
#print(dir(rwi))
#p.subplot(0, 0)
#p2.show(interactive_update=True)
#p.show(interactive_update=True)
#print(p2.render_window.IsCurrent())
#print(dir(p))

pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())

with pl.window_size_context((400, 400)):

    #pl.screenshot('/tmp/small_screenshot.png')
    pl.show(interactive_update=True)


with pl.window_size_context((500, 500)):

    #pl.screenshot('/tmp/big_screenshot.png')
    pl.show()
