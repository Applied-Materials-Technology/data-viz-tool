
from pathlib import Path
import os
from display_tools import *
from display_options import Displayer
from watcher import Watcher

#Adapt code to make this better for users 


my_displayer = Displayer(watch_path = Path(os.path.join(Path.cwd().parent.parent,"inputloc")))
my_displayer.echo_thing()
#print(my_displayer.__dict__)
print(my_displayer.test_display())
print(type(my_displayer.p))
my_watcher = Watcher(displayer = my_displayer)
print(my_watcher.displayer)
my_watcher.run()

