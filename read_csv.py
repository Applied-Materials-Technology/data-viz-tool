import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.colors import ListedColormap


points_csv = []
p = pv.Plotter(shape=(1,2))


p.subplot(0, 0)

raw_data = pd.read_csv("data/csvs/Image_0000_0.tiff.csv")

data2 = raw_data[['X[mm]', 'Y[mm]', 'Z[mm]', 'Strain-global frame: Exx', 'Strain-global frame: Eyy']]
data2.to_csv('newcsvfile.csv', index=False)



for i in range(len(raw_data['X[mm]'])):
    print(raw_data['X[mm]'][i])
    pointstemp = [raw_data['X[mm]'][i], raw_data['Y[mm]'][i], raw_data['Z[mm]'][i]]
    points_csv.append(pointstemp)

meshcsv = pv.PolyData(points_csv, force_float = False)



labels = dict(zlabel='Z', xlabel='X', ylabel='Y')

p.add_mesh(meshcsv, scalars = raw_data['Strain-global frame: Eyy'],show_scalar_bar=False)
p.show_grid(**labels)
p.add_axes(**labels)

p.add_scalar_bar(

    'Insert label')
 
points = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 

p.subplot(0,1)
mesh3 = pv.PolyData(points)



p.add_mesh(mesh3)

p.show()