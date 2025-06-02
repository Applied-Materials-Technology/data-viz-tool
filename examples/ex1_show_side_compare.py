
from pathlib import Path
import os
from dataviztool.display_tools import *
from dataviztool.display_options import Displayer
from dataviztool.watcher import Watcher
from copier import Copier

from threading import Thread

if not os.path.exists("example_inputloc"):
    os.makedirs("example_inputloc")
    os.makedirs("example_inputloc/left")
    os.makedirs("example_inputloc/right")

#my_displayer = Displayer(watch_path = Path(os.path.join(Path.cwd().parent.parent,"inputloc")))
my_displayer = Displayer(watch_path = "example_inputloc")
my_watcher = Watcher(displayer = my_displayer)
#my_watcher.watch_path = "example_inputloc"
print(my_watcher.displayer)
print(my_watcher.watch_path)

my_copier = Copier(os.path.join(Path.cwd().parent, "data/Data_viz"), "example_inputloc")

def start_watcher():
    my_watcher.run()

def start_copier():
    my_copier.start()

start_watcher()

