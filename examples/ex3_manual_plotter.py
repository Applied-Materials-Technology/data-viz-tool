
from pathlib import Path
import os
from dataviztool.displayer import Displayer
from dataviztool.displayopts import DisplayerOpts
from dataviztool.watcher import Watcher
#from copier import Copier

if not os.path.exists("example_inputloc"):
    os.makedirs("example_inputloc")
    os.makedirs("example_inputloc/left")
    os.makedirs("example_inputloc/right")

displayopts = DisplayerOpts()
#displayopts.set_csv_coords("X[mm]", "Y[mm]", "X[mm]", "Vertical Displacement V[mm]")

my_displayer = Displayer(automake_plotter=False, watch_path = "example_inputloc", display_opts=displayopts)

my_displayer.create_plotter(1,2)
my_displayer.assign_subplot(0,0,"Experimental View Manual", "left")
my_displayer.assign_subplot(0,1,"Simulation View Manual", "right")

print(my_displayer.display_opts.x_coord)
print(my_displayer.watch_path)

my_watcher = Watcher(displayer = my_displayer, watch_path="example_inputloc")


def start_watcher():
    my_watcher.run()

start_watcher()

