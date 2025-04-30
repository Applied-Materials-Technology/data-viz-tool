import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import time
import pandas as pd
from dataviztool.watcher import Watcher
from dataviztool.display_tools import auto_create_plotter

start_time = time.time()

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
                  watch_path = None,
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
        self.watch_path = watch_path
        self.make_labels = make_labels
        self._subplot_dict: dict = {}

        self.set_cmap(self.colourmap, self.colour_divs)

        self.set_clim_option(self.clim_option)

        if self.automake_plotter == True:

            auto_create_plotter(self)

        watcher = Watcher(self, watch_path=self.watch_path)


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

    def findme(self, displayer):
        print(displayer)



