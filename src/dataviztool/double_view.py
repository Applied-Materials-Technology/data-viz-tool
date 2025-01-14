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
import asyncio


start_time = time.time() # get base time to start timer

class WatcherCSV:

    watchDirectory = Path(os.path.join(Path.cwd().parent.parent, "inputloc"))

    def __init__(self):
        self.observer = Observer()
 
    def run(self):

        event_handler = HandlerCSV()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


 
class HandlerCSV(FileSystemEventHandler):

    """
    Decide what to do when certain events are detected in the watchDirectory
    """

    @staticmethod
    def on_any_event(event):
        
        #print(event.src_path)

        displayer.subplot_decider(event.src_path)

        if event.is_directory:

            return None
 
        elif event.event_type == 'created':

            #print("Watchdog received created event - % s." % event.src_path)

            pass

        elif event.event_type == 'modified':

            #print("Watchdog received modified event - % s." % event.src_path)

            pass


            if 'csv' in event.src_path:

                #For data in csv format, e.g. example csvs

                displayer.csv_displayer(event.src_path)

            else:

                #For reading tiff files

                displayer.tiff_displayer(event.src_path)

class Displayer():
    def __init__(self,
                  p = None, 
                  subploty: int = 1, 
                  x_coord: str = 'coor.X [mm]', 
                  y_coord: str = 'coor.Y [mm]', 
                  z_coord: str = 'coor.Z [mm]', 
                  colours: str = 'disp.Horizontal Displacement U [mm]', 
                  colourmap: str = 'viridis',
                  current_file: str = "",
                  automake_plotter: bool = True) -> None:
        
        self.p = p
        self.subploty = subploty
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord
        self.colours = colours
        self.colourmap = colourmap
        self.current_file = current_file
        self.automake_plotter = automake_plotter

        if self.automake_plotter == True:

            self.create_plotter()

    def create_plotter(self):

        """
        Create the plotter if not already defined
        """

        self.p = pv.Plotter(shape=(1,2))

    def subplot_decider(self, event):
        path1 = os.path.dirname(event)
        path2 = os.path.basename(path1)

        """Change subplot for different data"""
        if path2 == "right":
            self.subploty = 1
        elif path2 == "left":
            self.subploty = 0

    def csv_displayer(self, event):
        if self.current_file != event:

            self.p.subplot(0, self.subploty)
            points_csv = []
            raw_data = pd.read_csv(Path(os.path.join(event)), header=0)
            data2 = raw_data[[self.x_coord, self.y_coord, self.z_coord, self.colours]]


            for i in range(len(raw_data[self.x_coord])):
                pointstemp = [raw_data[self.x_coord][i], raw_data[self.y_coord][i], raw_data[self.z_coord][i]]
                points_csv.append(pointstemp)
            meshcsv = pv.PolyData(points_csv, force_float = False)

            print(time.time() - start_time)

            self.p.add_mesh(meshcsv, scalars = raw_data[self.colours],show_scalar_bar=False, interpolate_before_map = False)

            labels = dict(ztitle='Z', xtitle='X', ytitle='Y')
            self.p.show_bounds(**labels)

            self.p.add_scalar_bar('Label')

            self.p.camera_position = "xy"

            self.p.show(interactive=True, interactive_update = True)

            print(event)

            self.current_file = event

        else:
            #print("WAITING FOR FILE TRANSFER....")
            pass

    def tiff_displayer(self, event):
        if self.current_file != event:
            self.p.subplot(0,self.subploty)
            g = pv.read(Path(os.path.join(event)))
            print(time.time() - start_time)
            self.p.camera_position = "xy"
            self.p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar') # add the data from new file to the plotter
            self.p.show(interactive=True, interactive_update = True)
            self.p.update()
        else:
            #print("WAITING FOR FILE TRANSFER....")
            pass

    def set_csv_coords(self, choose_x, choose_y, choose_z, choose_c):

        """
        Set x, y, z and scalar values together
        """

        self.set_x_coord(choose_x)
        self.set_y_coord(choose_y)
        self.set_z_coord(choose_z)
        self.set_scalar_coord(choose_c)

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

    def set_scalar_coord(self, choose_c):

        """
        Choose what value from the csv to be the scalar value
        """
        
        self.c_coord = choose_c

    def set_cmap(self, colourmap):

        """
        Change the colour map from the selection of valid matplotlib colour maps
        """
        
        self.colourmap = plt.get_cmap(colourmap, 10)



if __name__ == '__main__':
    watch = WatcherCSV()
    displayer = Displayer()
    displayer.set_csv_coords('coor.X [mm]', 'coor.Y [mm]' ,'coor.Z [mm]', 'disp.Horizontal Displacement U [mm]')
    watch.run()

