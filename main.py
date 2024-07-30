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
start_time = time.time()

#print("--- %s seconds ---" % (time.time() - start_time))
#g = pv.read(Path(os.path.join(Path.cwd(), 'data/OptSpeckle_5Mpx_2464_2056_width5_8bit_GBlur1.tiff')))

counter = 0
p = pv.Plotter()
#p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar')
#p.show(interactive_update=True)
"""
def show(new_path):
    g = pv.read(Path(os.path.join(new_path)))
    p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar')"""


class OnMyWatch:
    watchDirectory = Path("example_generate")
 
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
 
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
 
        elif event.event_type == 'created':
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            print("Watchdog received modified event - % s." % event.src_path)
            try:
                #p.update()
                g = pv.read(Path(os.path.join(event.src_path)))
                print(event.src_path)
                print(time.time() - start_time)
                #print("file is okay")
                p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar')
                p.show(interactive_update=True)
                counter = counter + 1
                print(counter)
            except:
                print("WAITING FOR FILE TRANSFER....")
                #p.update()
             

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()

