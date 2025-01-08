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

########### full example requires pycdata ############

start_time = time.time() # get base time to start timer
#p = pv.Plotter(shape=(1,2)) # create plotter for pyvista

def test_function(texttoprint):
    print(texttoprint)

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
        path1 = os.path.dirname(event.src_path)
        path2 = os.path.basename(path1)

        """Change subplot for different data"""
        if path2 == "right":
            subploty = 1
        elif path2 == "left":
            subploty = 0


        if event.is_directory:
            return None
 
        elif event.event_type == 'created':
            #print("Watchdog received created event - % s." % event.src_path)
            pass

        elif event.event_type == 'modified':
            #print("Watchdog received modified event - % s." % event.src_path)
            pass

            """For data in csv format, e.g. example csvs """  
            if 'csv' in event.src_path:
                displayer.csv_displayer(subploty, event.src_path)
            else:
                """For reading tiff files"""
                displayer.tiff_displayer(subploty, event.src_path)

class Displayer():
    def __init__(self, p) -> None:
        self.p = p

    def csv_displayer(self, subploty, event):
        try:
            print("YOU ARE HERE")
            self.p.subplot(0, subploty)
            points_csv = []
            raw_data = pd.read_csv(Path(os.path.join(event)), header=0)
            #data2 = raw_data[['X[mm]', 'Y[mm]', 'Z[mm]', 'Strain-global frame: Exx', 'Strain-global frame: Eyy']]
            data2 = raw_data[['coor.X [mm]', 'coor.Y [mm]' ,'coor.Z [mm]', 'disp.Horizontal Displacement U [mm]']]

            #for i in range(len(raw_data['X[mm]'])):
            for i in range(len(raw_data['coor.X [mm]'])):
                #pointstemp = [raw_data['X[mm]'][i], raw_data['Y[mm]'][i], raw_data['Z[mm]'][i]]
                pointstemp = [raw_data['coor.X [mm]'][i], raw_data['coor.Y [mm]'][i], raw_data['coor.Z [mm]'][i]]
                points_csv.append(pointstemp)
            print("YOU ARE HERE 2")
            meshcsv = pv.PolyData(points_csv, force_float = False)

            #p.camera_position = "xy"
            #p.add_mesh(meshcsv, scalars = raw_data['Strain-global frame: Eyy'],show_scalar_bar=False)
            self.p.add_mesh(meshcsv, scalars = raw_data['disp.Horizontal Displacement U [mm]'],show_scalar_bar=False, interpolate_before_map = False)

            labels = dict(ztitle='Z', xtitle='X', ytitle='Y')
            self.p.show_bounds(**labels)

            self.p.add_scalar_bar('Label')

            self.p.camera_position = "xy"

            self.p.show(interactive=True, interactive_update = True)
            #p.update()
        except:
            pass

    def tiff_displayer(self, subploty, event):
        try:
            self.p.subplot(0,subploty)
            g = pv.read(Path(os.path.join(event)))
            self.p.camera_position = "xy"
            self.p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar') # add the data from new file to the plotter
            self.p.show(interactive=True, interactive_update = True)
            self.p.update()
        except:
            pass



if __name__ == '__main__':
    watch = WatcherCSV()
    displayer = Displayer(pv.Plotter(shape=(1,2)))
    watch.run()

