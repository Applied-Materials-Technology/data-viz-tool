from pathlib import Path
import os
from dataviztool.displayopts import *
from dataviztool.displayer import Displayer
from dataviztool.watcher import Watcher


my_displayer = Displayer(watch_path=Path("../inputloc"))
my_watcher = Watcher(displayer = my_displayer)
print(my_watcher.watch_path)
print(my_displayer.watch_path)
print(my_displayer.display_opts.x_coord)
my_watcher.set_watch_path(Path("../inputloc"))
print(f"Current watch_path: {my_displayer.watch_path}")
my_watcher.run()
