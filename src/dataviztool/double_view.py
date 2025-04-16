import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pyvista as pv
import os
import random
import time
import pandas as pd
import sys

#pv.global_theme.full_screen = True
#this breaks everything 

start_time = time.time() # get base time to start timer

class Watcher:

    """
    Watches the specified directory for new files
    """

    def __init__(self, watch_path: Path | None = None) -> None:
        if watch_path is None:
            self.watch_path = Path.cwd().parent.parent/"inputloc"
        else:
            self.watch_path = watch_path


        self.displayer = Displayer(automake_plotter=False)
        self.observer = Observer()

    def set_watch_path(self, watch_path: Path) -> None:
        self.watch_path = watch_path

    def run(self):

        event_handler = Handler()
        self.observer.schedule(event_handler, self.watch_path, recursive = True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    """
    Decide what to do when certain events are detected in the watchDirectory
    """

    @staticmethod
    def on_any_event(event):

        #displayer.subplot_decider(event.src_path)

        if event.is_directory:

            return None

        elif event.event_type == 'created':

            print("Watchdog received created event - % s." % event.src_path)

        elif event.event_type == 'modified':

            print("Watchdog received modified event - % s." % event.src_path)


            if 'csv' in event.src_path:

                #For data in csv format, e.g. example csvs

                displayer.display_csv(event.src_path)

            else:

                #For reading tiff files

                displayer.display_tiff(event.src_path)




class Displayer():

    """
    Class that handles the display options for the visualiser
    """
    def __init__(self,
                  p = None,
                  subploty: int = 1,
                  subplotx = 0,
                  x_coord: str = 'coor.X [mm]',
                  y_coord: str = 'coor.Y [mm]',
                  z_coord: str = 'coor.Z [mm]',
                  field: str = 'disp.Vertical Displacement V [mm]',
                  colourmap: str = 'viridis',
                  colour_divs: int = 10,
                  current_file: str = "",
                  automake_plotter: bool = True,
                  clim_option: str = 'default',
                  clim = None,
                  quan_min = None,
                  quan_max = None,
                  zoom_level: int = 1,
                  make_labels: int = 0) -> None:

        self.p = p
        self.subplotx = subplotx
        self.subploty = subploty
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord
        self.field = field
        self.colourmap = colourmap
        self.colour_divs = colour_divs
        self.current_file = current_file
        self.automake_plotter = automake_plotter
        self.clim_option = clim_option
        self.clim = clim
        self.quan_min =  quan_min,
        self.quan_max = quan_max,
        self.zoom_level = zoom_level
        self.make_labels = make_labels
        self._subplot_dict: dict = {}

        self.set_cmap(self.colourmap, self.colour_divs)

        self.set_clim_option(self.clim_option)

        if self.automake_plotter == True:

            self.auto_create_plotter()


    def set_csv_coords(self, choose_x, choose_y, choose_z, choose_field):

        """
        Set x, y, z and scalar values together
        """

        self.set_x_coord(choose_x)
        self.set_y_coord(choose_y)
        self.set_z_coord(choose_z)
        self.set_field_coord(choose_field)

    def set_x_coord(self, choose_x):

        """
        Choose what value from the csv to be the x coordinate
        """

        self.x_coord = choose_x

    def set_y_coord(self, choose_y):

        """
        Choose what value from the csv to be the y coordinate
        """

        self.y_coord = choose_y

    def set_z_coord(self, choose_z):

        """
        Choose what value from the csv to be the z coordinate
        """

        self.z_coord = choose_z

    def set_field_coord(self, choose_field):

        """
        Choose what value from the csv to be the scalar value
        """

        self.field = choose_field

    def set_cmap(self, colourmap, colour_divs):

        """
        Change the colour map from the selection of valid matplotlib colour maps
        """

        self.colourmap = plt.get_cmap(colourmap, colour_divs)

    def set_clim_option(self, clim_option, clim_min = 0, clim_max = 1, quan_min = .05, quan_max = .95):

        """
        default: min and max, variable throughout visualisation
        contained: locked to two value defined by user (or default min = 0, max = 1)
        """

        self.quan_min = quan_min

        self.quan_max = quan_max

        self.clim_option = clim_option

        if clim_option == 'contained':

            self.clim = [clim_min,clim_max]

    def set_zoom_level(self, zoom_level):

        """
        Choose what zoom level to display the plots
        """

        self.zoom_level = zoom_level

    def get_clim(self, csv_data):

        if self.clim_option == 'contained':
            pass

        elif self.clim_option == 'default':
            pass

        elif self.clim_option == 'quantile':

            clim_min = np.quantile(csv_data[self.field], self.quan_min)
            clim_max = np.quantile(csv_data[self.field], self.quan_max)

            self.clim = [clim_min, clim_max]

        elif self.clim_option == 'normal':

            """
            To update
            """

            sd = np.std(csv_data[self.field])

            clim_min = min(csv_data[self.field]) + sd
            clim_max = max(csv_data[self.field]) - sd

            self.clim = [clim_min, clim_max]

    def auto_create_plotter(self):

        """
        Create the plotter if not already defined
        """

        self.create_plotter(1,2)
        self.assign_subplot(0,0,"Experimental View", "left")
        self.assign_subplot(0,1,"Simulation View", "right")


    def create_plotter(self, xsize, ysize):

        """
        Create plotter of a specified size
        """

        self.p = pv.Plotter(shape=(xsize,ysize))

    def assign_subplot(self, subplotx, subploty, title = "", dirname = None):
        
        """
        Add the subplots to a dictionary with the directory that it should be linked with
        """
        dirlist = os.walk(watch.watch_path)
#        for i in dirlist:
#            print(i[1])
        #will probably end up too slow - only allow 0_1 folders?
        
        newlist = [x[1] for x in dirlist]
        print(newlist)
        """
        if dirname not in dirlist:
            make_dir = input("That directory could not be found, make directory? y/n").lower()
            if make_dir == "n":
                sys.exit()
            elif make_dir == "y":
                os.mkdir(watch.watch_path/dirname)"""

        if dirname is None:
            #fix to work with the above code
            dirname = str(subplotx) + "_" + str(subploty)
            print(dirname)

        self.p.subplot(subplotx, subploty)
        self.p.add_title(title)
        self._subplot_dict[dirname] = [subplotx, subploty]



    def subplot_decider(self, event: Path):
        path1 = os.path.dirname(event)
        path2 = os.path.basename(path1)

        """Change subplot for different data"""

        self.subplotx = self._subplot_dict[path2][0]
        self.subploty = self._subplot_dict[path2][1]

    def read_csv(self,event):

        """
        Read CSV data
        """

        points_csv = []
        raw_data = pd.read_csv(Path(os.path.join(event)), header=0)

        for i in range(len(raw_data[self.x_coord])):
            pointstemp = [raw_data[self.x_coord][i], raw_data[self.y_coord][i], raw_data[self.z_coord][i]]
            points_csv.append(pointstemp)
                
        meshcsv = pv.PolyData(points_csv, force_float = False)
        meshcsv[self.field] = raw_data[self.field]
        self.get_clim(raw_data)
        return meshcsv

    def display_csv(self, event):
        
        """
        Display read CSV data
        """

        #final modification event indicates file can be accessed
        #wait until a new file has been detected to know that the final event has happened
        if self.current_file != event:

            self.subplot_decider(event)
            self.p.subplot(self.subplotx, self.subploty)
            meshcsv = self.read_csv(event)

            print(time.time() - start_time)

            self.p.add_mesh(meshcsv,
                            scalars = self.field,
                            show_scalar_bar=False,
                            interpolate_before_map = False,
                            cmap = plt.get_cmap(self.colourmap, self.colour_divs),
                            clim = self.clim)

            if self.make_labels < 2:
                labels = dict(ztitle='Z', xtitle='X', ytitle='Y')
                self.p.show_bounds(**labels, mesh = meshcsv)
                self.make_labels = self.make_labels + 1

            self.p.add_scalar_bar(self.field)

            self.p.camera_position = "xy"
            self.p.zoom_camera(self.zoom_level)

            self.p.show(interactive=True, interactive_update = True)

            print(event)

            self.current_file = event

        else:
            print("WAITING FOR FILE TRANSFER....")

    def display_tiff(self, event):
        if self.current_file != event:
            self.p.subplot(0,self.subploty)
            g = pv.read(Path(os.path.join(event)))
            print(time.time() - start_time)
            self.p.camera_position = "xy"
            self.p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar') # add the data from new file to the plotter
            self.p.show(interactive=True, interactive_update = True)
            self.p.update()
        else:
            print("WAITING FOR FILE TRANSFER....")






if __name__ == '__main__':
    """
    watch_path = Path.home() / "data-viz-tool" / "temp_output"
    if not watch_path.is_dir():
        watch_path.mkdir()"""

    #watch = Watcher(watch_path)
    watch = Watcher(Path(os.path.join(Path.cwd().parent.parent,"inputloc")))
    #displayer = Displayer()
    displayer = Displayer(automake_plotter=False)

    """
    displayer.set_csv_coords('X[mm]',
                             'Y[mm]',
                             'Z[mm]',
                             'Vertical Displacement V[mm]')"""
    
    displayer.create_plotter(2,2)
    displayer.assign_subplot(0,0,"Experimental View", "left")
    displayer.assign_subplot(0,1,"Simulation View", "right")
    displayer.assign_subplot(1,0,"Experimental View 2", "left2")
    displayer.assign_subplot(1,1,"Simulation View 2", "right2")
    
    displayer.set_csv_coords('coor.X [mm]',
                             'coor.Y [mm]',
                             'coor.Z [mm]',
                             'disp.Vertical Displacement V [mm]')

    displayer.set_clim_option('normal')
    watch.run()

