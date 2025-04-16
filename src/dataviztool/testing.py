
from pathlib import Path
import os
from display_tools import *
from display_options import Displayer
from watcher import Watcher

my_displayer = Displayer(watch_path = Path(os.path.join(Path.cwd().parent.parent,"inputloc")))
my_watcher = Watcher(displayer = my_displayer)
print(my_watcher.displayer)
my_watcher.run()
