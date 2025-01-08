import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from pathlib import Path
import os



from matplotlib.colors import ListedColormap



csv_path = "data/csvs"
files_set1 = [Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0001_0.tiff.csv")), Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0002_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0003_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0004_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0005_0.tiff.csv"))]
files_set2 = [Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0006_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0007_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0008_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0009_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0010_0.tiff.csv"))]
file_set_full = [Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0001_0.tiff.csv")), Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0002_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0003_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0004_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0005_0.tiff.csv")), Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0006_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0007_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0008_0.tiff.csv")),
         Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0009_0.tiff.csv")),Path(os.path.join(Path.cwd().parent,"data/csvs/Image_0010_0.tiff.csv"))]


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

display()

