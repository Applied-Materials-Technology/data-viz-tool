"""
Creates plotter, configures subplots, and plots the data for a displayer
"""


import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import time
import pandas as pd
from dataviztool.displayopts import DisplayerOpts
#from logger import logger


class Displayer():

    def __init__(self,
                p = None,
                automake_plotter = True,
                display_opts = DisplayerOpts()) -> None:
        
        self.p = p
        self.automake_plotter = automake_plotter
        self.display_opts = display_opts

        self.display_opts.watch_path = Path(os.path.join(Path.cwd().parent.parent,"inputloc"))

        if self.automake_plotter == True:
            self.auto_create_plotter()

    def auto_create_plotter(self):

        """
        Create the plotter if not already defined


        Parameters
        ----------

        displayer: display_options.Displayer
            The displayer to create a plotter and subplots for.
        """

        self.create_plotter(1,2)
        self.assign_subplot(0,0,"Experimental View", "left")
        self.assign_subplot(0,1,"Simulation View", "right")


    def create_plotter(self, 
                    xsize: int, 
                    ysize: int):

        """
        Create plotter of a specified size

        Parameters
        ----------

            displayer : display_options.Displayer
                The displayer to create a plotter and subplots for.
            xsize : (int)
                the number sub-render windows to make inside of the main window horizontally
            ysize : (int)
                the number sub-render windows to make inside of the main window vertically

        Returns
        -------

            displayer.p : pyvista.plotting.plotter.Plotter
                The plotter associated with the Displayer object displayer
        """

        self.p = pv.Plotter(shape=(xsize,ysize))
        return self.p

    def assign_subplot(self, 
                    subplotx: int, 
                    subploty: int, 
                    title: str = "", 
                    dirname: Path = None):
            
            """
            Add the subplots to a dictionary with the directory that it should be linked with

            Parameters
            ----------

                displayer : display_options.Displayer
                    The displayer object to reference
                subplotx : (int)
                    the number of the sub-render window to reference inside of the main window horizontally
                subploty : (int) 
                    the number sub-render window to reference inside of the main window vertically
                title : (str) 
                    the text that should be displayed in the subplot references by subplotx,subploty
                dirname : (path)
                    path to the directory that will contain the data that will be displayed by the referenced subplot
            """
            dirlist = os.walk(self.display_opts.watch_path)
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

            self.p.subplot(subplotx, subploty)
            self.p.add_title(title)
            self.display_opts._subplot_dict[dirname] = [subplotx, subploty]



    def subplot_decider(self, 
                        event: Path):

        """
        Change subplot for different data
        
        Parameters
        ----------
            displayer : display_options.Displayer
                The displayer object to reference.
            xsize : (int)
                the number sub-render windows inside of the main window horizontally
            ysize : (int)
                the number sub-render windows inside of the main window vertically
        """

        path1 = os.path.dirname(event)
        path2 = os.path.basename(path1)

        self.display_opts.subplotx = self.display_opts._subplot_dict[path2][0]
        self.display_opts.subploty = self.display_opts._subplot_dict[path2][1]

    def read_csv(self,
                event: Path):

        """
        Read CSV data
        
        Parameters:
        ----------
            displayer : display_options.Displayer
                The displayer object to reference.
            event : path
                the path to the file of the event detected by watchdog watcher
        """

        points_csv = []
        raw_data = pd.read_csv(Path(os.path.join(event)), header=0)

        for i in range(len(raw_data[self.display_opts.x_coord])):
            pointstemp = [raw_data[self.display_opts.x_coord][i], raw_data[self.display_opts.y_coord][i], raw_data[self.display_opts.z_coord][i]]
            points_csv.append(pointstemp)
                
        meshcsv = pv.PolyData(points_csv, force_float = False)
        meshcsv[self.display_opts.field] = raw_data[self.display_opts.field]
        self.display_opts.get_clim(raw_data)
        return meshcsv


    def display_csv(self,
                    event: Path):
        
        """
        Display read CSV data

        Parameters
        ----------
            displayer : display_options.Displayer
                The displayer object to reference.
            event : path
                the path to the file of the event detected by watchdog watcher
        """


        """
        final modification event indicates file can be accessed
        wait until a new file has been detected to know that the final event has happened
        """

        if self.display_opts.current_file != event:
            self.subplot_decider(event)
            self.p.subplot(self.display_opts.subplotx, self.display_opts.subploty)
            meshcsv = self.read_csv(event)

            self.p.add_mesh(meshcsv,
                            scalars = self.display_opts.field,
                            show_scalar_bar=False,
                            interpolate_before_map = False,
                            cmap = plt.get_cmap(self.display_opts.colourmap, self.display_opts.colour_divs),
                            clim = self.display_opts.clim)

            if self.display_opts.make_labels < 2:
                labels = dict(ztitle='Z', xtitle='X', ytitle='Y')
                self.p.show_bounds(**labels, mesh = meshcsv)
                self.display_opts.make_labels = self.display_opts.make_labels + 1

            self.p.add_scalar_bar(self.display_opts.field)

            self.p.camera_position = "xy"
            self.p.zoom_camera(self.display_opts.zoom_level)

            self.p.show(interactive=True, interactive_update = True)

            print(event)

            self.display_opts.current_file = event

        else:
            print("WAITING FOR FILE TRANSFER....")

    def display_tiff(self, 
                    event: Path):

        """
        Parameters
        ----------
            displayer : display_options.Displayer
                The displayer object to reference.
            event : path
                the path to the file of the event detected by watchdog watcher
        """

        if self.display_opts.current_file != event:
            self.p.subplot(0,self.display_opts.subploty)
            g = pv.read(Path(os.path.join(event)))
            self.p.camera_position = "xy"
            self.p.add_mesh(g, opacity=0.5, name='data', cmap='gist_ncar') # add the data from new file to the plotter
            self.p.show(interactive=True, interactive_update = True)
            self.p.update()
        else:
            print("WAITING FOR FILE TRANSFER....")
            #logger.info()

    
    def test_display(self):
        self.p.show()