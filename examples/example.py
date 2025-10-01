from dataviztool.displayer import Displayer
from dataviztool.displayopts import DisplayerOpts
from dataviztool.watcher import Watcher
from copier import Copier

my_displayer = Displayer(watch_path = "example_inputloc")
my_watcher = Watcher(displayer = my_displayer)

my_displayer.p.show()