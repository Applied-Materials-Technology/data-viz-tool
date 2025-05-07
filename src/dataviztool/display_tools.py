import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import time
import pandas as pd

start_time = time.time()

def auto_create_plotter(displayer):

    """
    Create the plotter if not already defined


    Parameters:
        displayer: The displayer to create a plotter and subplots for.
    """

    create_plotter(displayer,1,2)
    assign_subplot(displayer, 0,0,"Experimental View", "left")
    assign_subplot(displayer, 0,1,"Simulation View", "right")


def create_plotter(displayer, xsize, ysize):

    """
    Create plotter of a specified size

    Parameters:
        displayer: The displayer to create a plotter and subplots for.
        xsize (int): the number sub-render windows to make inside of the main window horizontally
        ysize (int): the number sub-render windows to make inside of the main window vertically
    """

    displayer.p = pv.Plotter(shape=(xsize,ysize))

def assign_subplot(displayer, subplotx, subploty, title = "", dirname = None):
        
        """
        Add the subplots to a dictionary with the directory that it should be linked with

        Parameters:
            displayer: The displayer object to reference
            subplotx (int): the number of the sub-render window to reference inside of the main window horizontally
            subploty (int): the number sub-render window to reference inside of the main window vertically
            title (str): the text that should be displayed in the subplot references by subplotx,subploty
            dirname (path): path to the directory that will contain the data that will be displayed by the referenced subplot
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

    """
    Change subplot for different data
    
    Parameters:
        displayer: The displayer object to reference.
        xsize (int): the number sub-render windows inside of the main window horizontally
        ysize (int): the number sub-render windows inside of the main window vertically
    """

    path1 = os.path.dirname(event)
    path2 = os.path.basename(path1)

    displayer.subplotx = displayer._subplot_dict[path2][0]
    displayer.subploty = displayer._subplot_dict[path2][1]

def read_csv(displayer,event):

    """
    Read CSV data
    
    Parameters:
        displayer: The displayer object to reference.
        event: the path to the file of the event detected by watchdog watcher
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


def display_csv(displayer,event):
    
    """
    Display read CSV data

    Parameters:
        displayer: The displayer object to reference.
        event: the path to the file of the event detected by watchdog watcher
    """

    #final modification event indicates file can be accessed
    #wait until a new file has been detected to know that the final event has happened
    if displayer.current_file != event:
        #print(event)
        subplot_decider(displayer, event)
        displayer.p.subplot(displayer.subplotx, displayer.subploty)
        meshcsv = read_csv(displayer, event)

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

    """
    Display data from tiff files

    Parameters:
        displayer: The displayer object to reference.
        event: the path to the file of the event detected by watchdog watcher
    """

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