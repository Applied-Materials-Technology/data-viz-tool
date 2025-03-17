import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from pathlib import Path
import os
import shutil

class Copier():
    def __init__(self, halfpath, destination, current_file = "") -> None:
        self.filelist = []
        self.halfpath = halfpath
        self.destination = destination
        self.current_file = ""


    def join_path(self, filename):
        self.current_file = Path(os.path.join(self.halfpath, filename))

    def get_path(self):
        #for filename in os.listdir(Path(os.path.join(self.halfpath))):
        file_list = sorted([ f for f in os.listdir(Path(os.path.join(self.halfpath)))])
        for filename in file_list:
            self.join_path(filename)
            self.write_file()

    def write_file(self):
        shutil.copy(self.current_file, Path(os.path.join(self.destination, "left")))
        #time.sleep(1)
        shutil.copy(self.current_file, Path(os.path.join(self.destination, "right")))
        #time.sleep(1)
        #print(Path(os.path.join(self.destination, "left")))
        #print(Path(os.path.join(self.destination, "right")))




my_copier = Copier(os.path.join(Path.cwd().parent, "data/Data_viz"), os.path.join(Path.cwd().parent, "inputloc"))
my_copier.get_path()