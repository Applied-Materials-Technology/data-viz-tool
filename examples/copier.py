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

    def start(self):
        print("starting copying files...")
        self.get_path()

    def join_path(self, filename):
        self.current_file = Path(os.path.join(self.halfpath, filename))

    def get_path(self):
        file_list = sorted([ f for f in os.listdir(Path(os.path.join(self.halfpath)))])
        for filename in file_list:
            self.join_path(filename)
            self.write_file()

    def write_file(self):
        shutil.copy(self.current_file, Path(os.path.join(self.destination, "left")))
        shutil.copy(self.current_file, Path(os.path.join(self.destination, "right")))


