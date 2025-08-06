from pathlib import Path
import os
from displayopts import *
from displayer import Displayer
from watcher import Watcher

my_displayer = Displayer()
#my_displayer.create_plotter(1,1)
#my_displayer.assign_subplot(0,0,"New View", "new")
#print(my_displayer.test_display())
#print(type(my_displayer.p))
my_watcher = Watcher(displayer = my_displayer)
print(my_watcher.watch_path)
my_watcher.run()