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


p = pv.Plotter(shape=(1,2))


#p.subplot(0, 0)
#p.show(interactive_update=True)




def read_csv(file):
    raw_data = pd.read_csv(file, header=0)

    data2 = raw_data[['X[mm]', 'Y[mm]', 'Z[mm]', 'Strain-global frame: Exx', 'Strain-global frame: Eyy']]
    points_csv = []


    for i in range(len(raw_data['X[mm]'])):
        print(raw_data['X[mm]'][i])
        pointstemp = [raw_data['X[mm]'][i], raw_data['Y[mm]'][i], raw_data['Z[mm]'][i]]
        points_csv.append(pointstemp)
    print(f"{np.max(raw_data['X[mm]'][:])=}")
    print(f"{np.min(raw_data['X[mm]'][:])=}")
    print(f"{np.max(raw_data['Y[mm]'][:])=}")
    print(f"{np.min(raw_data['Y[mm]'][:])=}")
    print(f"{np.max(raw_data['Z[mm]'][:])=}")
    print(f"{np.min(raw_data['Z[mm]'][:])=}")
    meshcsv = pv.PolyData(points_csv, force_float = False)
    show_csv2(meshcsv, raw_data)

def show_csv(meshcsv, raw_data):
    p.subplot(0, 0)
    p.clear()
    p.update()
    labels = dict(ztitle='Z', xtitle='X', ytitle='Y')
    p.add_mesh(meshcsv, scalars = raw_data['Strain-global frame: Eyy'],show_scalar_bar=False)
    p.show_bounds(**labels)

    p.add_scalar_bar(

    'Label')


    p.show(interactive_update=True)
    p.update()
    p.camera_position = "xy"
    time.sleep(5)

def show_csv2(meshcsv, raw_data):
    p.add_mesh(meshcsv, scalars = raw_data['Strain-global frame: Eyy'],show_scalar_bar=False) # add the data from new file to the plotter
    p.show(interactive=True, interactive_update = True)
    p.update()
    p.close()


from threading import Thread

def func1():
    for file in files_set1:
        read_csv(file)

def func2():
    print("Working")

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()