import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import time
import pandas as pd

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

def auto_create_plotter(displayer):

    """
    Create the plotter if not already defined
    """

    create_plotter(displayer,1,2)
    assign_subplot(displayer, 0,0,"Experimental View", "left")
    assign_subplot(displayer, 0,1,"Simulation View", "right")


def create_plotter(displayer, xsize, ysize):

    """
    Create plotter of a specified size
    """

    displayer.p = pv.Plotter(shape=(xsize,ysize))

def assign_subplot(displayer, subplotx, subploty, title = "", dirname = None):
        
        """
        Add the subplots to a dictionary with the directory that it should be linked with
        """
        dirlist = os.walk(displayer.watch_path)
#        for i in dirlist:
#            print(i[1])
        #will probably end up too slow - only allow 0_1 folders?
        
        newlist = [x[1] for x in dirlist]
        print(newlist)
        """
        if dirname not in dirlist:
            make_dir = input("That directory could not be found, make directory? y/n").lower()
            if make_dir == "n":
                sys.exit()
            elif make_dir == "y":
                os.mkdir(watch.watch_path/dirname)"""

        if dirname is None:
            #fix to work with the above code
            dirname = str(subplotx) + "_" + str(subploty)
            print(dirname)

        displayer.p.subplot(subplotx, subploty)
        displayer.p.add_title(title)
        displayer._subplot_dict[dirname] = [subplotx, subploty]



def subplot_decider(displayer, event: Path):
    path1 = os.path.dirname(event)
    path2 = os.path.basename(path1)

    """Change subplot for different data"""

    displayer.subplotx = displayer._subplot_dict[path2][0]
    displayer.subploty = displayer._subplot_dict[path2][1]

def read_csv(displayer,event):

    """
    Read CSV data
    """

    points_csv = []
    raw_data = pd.read_csv(Path(os.path.join(event)), header=0)

    for i in range(len(raw_data[displayer.x_coord])):
        pointstemp = [raw_data[displayer.x_coord][i], raw_data[displayer.y_coord][i], raw_data[displayer.z_coord][i]]
        points_csv.append(pointstemp)
            
    meshcsv = pv.PolyData(points_csv, force_float = False)
    meshcsv[displayer.field] = raw_data[displayer.field]
    displayer.get_clim(raw_data)
    return meshcsv

def display_csv(displayer, event):
    
    """
    Display read CSV data
    """

    #final modification event indicates file can be accessed
    #wait until a new file has been detected to know that the final event has happened
    if displayer.current_file != event:

        subplot_decider(event)
        displayer.p.subplot(displayer.subplotx, displayer.subploty)
        meshcsv = read_csv(event)

        print(time.time() - start_time)

        displayer.p.add_mesh(meshcsv,
                        scalars = displayer.field,
                        show_scalar_bar=False,
                        interpolate_before_map = False,
                        cmap = plt.get_cmap(displayer.colourmap, displayer.colour_divs),
                        clim = displayer.clim)

        if displayer.make_labels < 2:
            labels = dict(ztitle='Z', xtitle='X', ytitle='Y')
            displayer.p.show_bounds(**labels, mesh = meshcsv)
            displayer.make_labels = displayer.make_labels + 1

        displayer.p.add_scalar_bar(displayer.field)

        displayer.p.camera_position = "xy"
        displayer.p.zoom_camera(displayer.zoom_level)

        displayer.p.show(interactive=True, interactive_update = True)

        print(event)

        displayer.current_file = event

    else:
        print("WAITING FOR FILE TRANSFER....")

def display_tiff(displayer, event):
    if displayer.current_file != event:
        displayer.p.subplot(0,displayer.subploty)
        g = pv.read(Path(os.path.join(event)))
        print(time.time() - start_time)
        displayer.p.camera_position = "xy"
        displayer.p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar') # add the data from new file to the plotter
        displayer.p.show(interactive=True, interactive_update = True)
        displayer.p.update()
    else:
        print("WAITING FOR FILE TRANSFER....")

