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

########### requires pycdata ############

start_time = time.time() # get base time to start timer

p = pv.Plotter() # create plotter for pyvista


class Watcher:
    watchDirectory = Path("example_generate") # path where data is being read from
 
    def __init__(self):
        self.observer = Observer()
 
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
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
        if event.is_directory:
            return None
 
        elif event.event_type == 'created':
            print("Watchdog received created event - % s." % event.src_path)

        elif event.event_type == 'modified':
            print("Watchdog received modified event - % s." % event.src_path)  
            try:
                g = pv.read(Path(os.path.join(event.src_path)))
                print(event.src_path)
                print(time.time() - start_time)
                print("FILE ACCEPTED")
                p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar') # add the data from new file to the plotter
                p.show(interactive=True, interactive_update = True)
                p.update()
            except:
                print("WAITING FOR FILE TRANSFER....") # error occurs when trying to open a file before it's fully uploaded
             

if __name__ == '__main__':
    watch = Watcher()
    watch.run()

