import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from pathlib import Path
import os



from matplotlib.colors import ListedColormap



csv_path = "data/csvs"
csv_path2 = "data/Data_viz"
half_path = os.path.join(Path.cwd().parent, "data/Data_viz")
files_set1_old = [Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0001_0.tiff.csv")), Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0002_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0003_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0004_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0005_0.tiff.csv"))]
files_set2_old = [Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0006_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0007_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0008_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0009_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0010_0.tiff.csv"))]
file_set_full_old = [Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0001_0.tiff.csv")), Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0002_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0003_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0004_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0005_0.tiff.csv")), Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0006_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0007_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0008_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0009_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0010_0.tiff.csv"))]

file_names = sorted([ f for f in os.listdir(Path(os.path.join(Path.cwd().parent, csv_path2)))])
file_set_full = [Path(os.path.join(half_path, i)) for i in file_names]
#print(file_set_full2)

p = pv.Plotter(shape=(1,2))


def read_csv(file, subplot):

    raw_data = pd.read_csv(file, header=0)

    data2 = raw_data[['X[mm]', 'Y[mm]', 'Z[mm]', 'Strain-global frame: Exx', 'Strain-global frame: Eyy']]
    points_csv = []


    for i in range(len(raw_data['X[mm]'])):
        pointstemp = [raw_data['X[mm]'][i], raw_data['Y[mm]'][i], raw_data['Z[mm]'][i]]
        points_csv.append(pointstemp)
    meshcsv = pv.PolyData(points_csv, force_float = False)
    show_csv(meshcsv, raw_data, subplot)



def show_csv(meshcsv, raw_data, subplot):
    p.subplot(0,subplot)
    p.show(interactive_update=True)
    p.add_mesh(meshcsv, scalars = raw_data['Strain-global frame: Eyy'],show_scalar_bar=False) # add the data from new file to the plotter
    p.show(interactive=True, interactive_update = True)
    p.camera_position = "xy"
    labels = dict(ztitle='Z', xtitle='X', ytitle='Y')
    p.show_bounds(**labels)
    p.add_scalar_bar(

    'Label')
    p.update()
    #time.sleep(5)


def display():
    for file in file_set_full:
        read_csv(file, 0)
        read_csv(file,1)


#display()

def csv_displayer(file, subploty):

    x_coord = 'coor.X [mm]'
    y_coord = 'coor.Y [mm]'
    z_coord = 'coor.Z [mm]'
    colours = 'disp.Vertical Displacement V [mm]'

    p.subplot(0, subploty)
    points_csv = []
    #raw_data = pd.read_csv(Path(os.path.join(event)), header=0)
    raw_data = pd.read_csv(file)
    data2 = raw_data[[x_coord, y_coord, z_coord, colours]]


    for i in range(len(raw_data[x_coord])):
        pointstemp = [raw_data[x_coord][i], raw_data[y_coord][i], raw_data[z_coord][i]]
        points_csv.append(pointstemp)
    meshcsv = pv.PolyData(points_csv, force_float = False)


    p.add_mesh(meshcsv, color='magenta', scalars = raw_data[colours],show_scalar_bar=False, interpolate_before_map = False, cmap = plt.get_cmap("gist_grey  ", 10))

    labels = dict(ztitle='Z', xtitle='X', ytitle='Y')
    p.show_bounds(**labels)

    p.add_scalar_bar('Label')

    p.camera_position = "xy"

    p.show(interactive=True, interactive_update = True)


def display2():
    for file in file_set_full:
        csv_displayer(file, 0)
        csv_displayer(file,1)

display2()