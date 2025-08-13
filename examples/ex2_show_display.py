from pathlib import Path
import os
from dataviztool.displayopts import *
from dataviztool.displayer import Displayer
from dataviztool.watcher import Watcher

#my_displayer = Displayer(watch_path = "/home/vc9387/code/data-viz-tool/inputloc")
my_displayer = Displayer()
my_watcher = Watcher(displayer = my_displayer, watch_path = "path1")


print(my_displayer.watch_path)
my_watcher.set_watch_path("../inputloc")
print(my_displayer.watch_path)
my_watcher.run()
