from __future__ import annotations
import numpy as np
import pyvista as pv
from dataclasses import dataclass



import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import time
import pandas as pd
import json
from dataviztool.watcher import Watcher
#from logger import logger

start_time = time.time()

@dataclass
class DisplayerOpts():

    """
    Class that handles the display options for the visualiser
    """      

    def __init__(self,
                  p = None,
                  subploty: int = 1,
                  subplotx: int = 0,
                  x_coord: str = 'coor.X [mm]',
                  y_coord: str = 'coor.Y [mm]',
                  z_coord: str = 'coor.Z [mm]',
                  field: str = 'disp.Vertical Displacement V [mm]',
                  colourmap: str = 'viridis',
                  colour_divs: int = 10,
                  current_file: str = "",
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
        self.clim_option = clim_option
        self.clim = clim
        self.quan_min =  quan_min,
        self.quan_max = quan_max,
        self.zoom_level = zoom_level
        self.make_labels = make_labels


        self.set_cmap(self.colourmap, self.colour_divs)

        self.set_clim_option(self.clim_option)


    def echo_thing(self):
        #logger.info('hello from echo thing')
        pass

    def set_csv_coords(self, 
                       choose_x: str, 
                       choose_y: str, 
                       choose_z: str, 
                       choose_field: str):

        """
        Set x, y, z and scalar values together

        Parameters
        ----------

            choose_x : str
                What should be set to be read as the x coordinate.
            choose_y : str
                What should be set to be read as the y coordinate.
            choose_z : str
                What should be set to be read as the z coordinate.
            choose_field : str
                What should be chosen to be read as the scalar field.
        """

        self.set_x_coord(choose_x)
        self.set_y_coord(choose_y)
        self.set_z_coord(choose_z)
        self.set_field_coord(choose_field)

    def set_x_coord(self, 
                    choose_x: str):

        """
        Choose what value from the csv to be the x coordinate

        Parameters
        ----------

            choose_x : str
                What should be set to be read as the x coordinate.
        """

        self.x_coord = choose_x

    def set_y_coord(self, 
                    choose_y: str):

        """
        Choose what value from the csv to be the y coordinate

        Parameters
        ----------

            choose_y : str
                What should be set to be read as the y coordinate.
        """

        self.y_coord = choose_y

    def set_z_coord(self, 
                    choose_z: str):

        """
        Choose what value from the csv to be the z coordinate

        Parameters
        ----------

            choose_z : str
                What should be set to be read as the z coordinate.
        """

        self.z_coord = choose_z

    def set_field_coord(self, 
                        choose_field: str):

        """
        Choose what value from the csv to be the scalar value

        Parameters
        ----------

            choose_field : str
                What should be set to be read as the scalar value.
        """

        self.field = choose_field

    def set_cmap(self, 
                 colourmap: str, 
                 colour_divs: int):

        """
        Change the colour map from the selection of valid matplotlib colour maps

        Parameters
        ----------

            colourmap : str
                Colour map from selection of valid matplotlib colour maps.
            colour_divs : str
                plt.get_cmap luv.
        """

        self.colourmap = plt.get_cmap(colourmap, colour_divs)

    def set_clim_option(self, 
                        clim_option: str, 
                        clim_min: int = 0, 
                        clim_max: int = 1, 
                        quan_min: float = .05, 
                        quan_max: float = .95):

        """
        default: min and max, variable throughout visualisation
        contained: locked to two value defined by user (or default min = 0, max = 1)

        Parameters
        ----------

            clim_options : str
                Method of controlling the range of the colour bar 
            clim_min : int
                Min value for colourbar
            clim_max : int
                Max value for colourbar
            quan_min : float
                Min quantile %
            quan_max : float
                Max quantile %
        """

        self.quan_min = quan_min

        self.quan_max = quan_max

        self.clim_option = clim_option

        if clim_option == 'contained':

            self.clim = [clim_min,clim_max]

    def set_zoom_level(self, 
                       zoom_level: float):

        """
        Choose what zoom level to display the plots

        Parameters
        ----------

            zoom_level : float
                Set the zoom level in the plotter
        """

        self.zoom_level = float(zoom_level)

    def set_watch_path(self, watch_path):

        """
        Choose the path that will be watched for incoming files to be displayed

        Parameters
        ----------

            watch_path : Path
                The path that will be watched for incoming files to be displayed
        """

        self.watch_path = watch_path

    def get_clim(self, 
                 csv_data):

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

    def test_display(self):
        self.p.show()
        
        




    
