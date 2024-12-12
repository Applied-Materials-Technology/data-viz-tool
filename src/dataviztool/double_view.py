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

p = pv.Plotter(shape=(1,2)) # create plotter for pyvista


class WatcherCSV:
    #watchDirectory = Path("examples") # path where data is being read from
    watchDirectory = Path(os.path.join(Path.cwd().parent.parent, "examples"))
 
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
        if event.is_directory:
            return None
 
        elif event.event_type == 'created':
            print("Watchdog received created event - % s." % event.src_path)

        elif event.event_type == 'modified':
            print("Watchdog received modified event - % s." % event.src_path)  
            if 'exdata' in event.src_path:
                try:
                    p.subplot(0, 0)
                    #g = pv.read(Path(os.path.join(event.src_path)))
                    points_csv = []
                    raw_data = pd.read_csv(Path(os.path.join(event.src_path)), header=0)
                    data2 = raw_data[['X[mm]', 'Y[mm]', 'Z[mm]', 'Strain-global frame: Exx', 'Strain-global frame: Eyy']]

                    for i in range(len(raw_data['X[mm]'])):
                        #print(raw_data['X[mm]'][i])
                        pointstemp = [raw_data['X[mm]'][i], raw_data['Y[mm]'][i], raw_data['Z[mm]'][i]]
                        points_csv.append(pointstemp)
                    meshcsv = pv.PolyData(points_csv, force_float = False)
                    p.add_mesh(meshcsv, scalars = raw_data['Strain-global frame: Eyy'],show_scalar_bar=False)
                    print(event.src_path)
                    #print(time.time() - start_time)
                    #print("FILE ACCEPTED")
                    #p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar') # add the data from new file to the plotter
                    p.show(interactive=True, interactive_update = True)
                    p.update()
                except:
                    print("WAITING FOR FILE TRANSFER....") # error occurs when trying to open a file before it's fully uploaded
            else:
                print("Watchdog received modified event - % s." % event.src_path)  
                try:
                    p.subplot(0,1)
                    g = pv.read(Path(os.path.join(event.src_path)))
                    print(event.src_path)
                    print(time.time() - start_time)
                    print("FILE ACCEPTED")
                    p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar') # add the data from new file to the plotter
                    p.show(interactive=True, interactive_update = True)
                    p.update()
                except:
                    print("WAITING FOR FILE TRANSFER....") # error occurs when trying to open a file before it's fully uploaded

#make periodic functions here
async def plot_side_one():
    await asyncio.sleep(1)
    print("FUNC1")
    watch = WatcherCSV()
    watch.run()

async def plot_side_two():
    print("Starting another task...")
    await asyncio.sleep(1)
    watch = WatcherCSV()
    watch.run()

async def main():
    await asyncio.gather(
        plot_side_one(),
        plot_side_two(),
    )

if __name__ == '__main__':
    asyncio.run(main())

