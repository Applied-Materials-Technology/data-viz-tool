from visualiser import Visualiser 
from visualiser import Watcher
from pathlib import Path
import os

my_visual = Visualiser()

"""
my_visual.displayer.create_plotter(2,2)
my_visual.displayer.assign_subplot(0,0,"Experimental View", "left")
my_visual.displayer.assign_subplot(0,1,"Simulation View", "right")
#my_visual.displayer.assign_subplot(1,0,"Experimental View 2", "left2")
#my_visual.displayer.assign_subplot(1,1,"Simulation View 2", "right2")

#my_visual.assign_subplot2(0,0,"Experimental View", "left")
#my_visual.assign_subplot2(0,1,"Simulation View", "right")



my_visual.displayer.set_csv_coords('coor.X [mm]',
                            'coor.Y [mm]',
                            'coor.Z [mm]',
                            'disp.Vertical Displacement V [mm]')

my_visual.displayer.set_clim_option('normal')
my_visual.watcher.run()

#my_visual.show_path()"""

#my_visual2 = Watcher(Path(os.path.join(Path.cwd().parent.parent,"inputloc")))

#print(my_visual2.displayer)

#from displayer import Displayer
from displayer import *
from watcher import Watcher

my_displayer = Displayer(watch_path = Path(os.path.join(Path.cwd().parent.parent,"inputloc")))
my_watcher = Watcher(displayer = my_displayer)
print(my_watcher.displayer)
my_watcher.run()
#my_watcher = Watcher(Path(os.path.join(Path.cwd().parent.parent,"inputloc")))

#my_displayer = Displayer()