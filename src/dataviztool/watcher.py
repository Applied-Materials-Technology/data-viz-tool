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
from displayer import *

#pv.global_theme.full_screen = True
#this breaks everything 

start_time = time.time() # get base time to start timer

class Watcher:

    """
    Watches the specified directory for new files
    """

    def __init__(self, displayer, watch_path: Path | None = None) -> None:
        if watch_path is None:
            self.watch_path = Path.cwd().parent.parent/"inputloc"
        else:
            self.watch_path = watch_path


        self.displayer = displayer
        self.observer = Observer()

    def set_watch_path(self, watch_path: Path) -> None:
        self.watch_path = watch_path

    def run(self):

        event_handler = Handler()
        event_handler.set_displayer(self.displayer)
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

                display_csv(watcher.displayer, event.src_path)

            else:

                #For reading tiff files

                display_tiff(watcher.displayer, event.src_path)


"""
class MyEventHandler(PatternMatchingEventHandler):
    def hook(self, thing):
        self.thing = thing
    def on_modified(self, event):
        super(MyEventHandler, self).on_modified(event)
        logging.info("File %s was just modified" % event.src_path)
        self.thing.readConfigFile()  #<- i want to call this method in class Configuration

class MainClass:
    def __init__(self):
        self.conf = Configuration()
        event_handler = MyEventHandler(patterns=patterns)
        event_handler.hook(self.conf)"""