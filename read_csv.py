import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.colors import ListedColormap

#pv.set_plot_theme(pv.themes.ParaViewTheme())
points_csv = []
p = pv.Plotter(shape=(1,2))
#p = pv.Plotter()
p.subplot(0, 0)
#mesh1 = pv.read('data/stc-thermomech-basic-bcbase_out.e')
#mesh1 = pv.PolyData('data/Image_0006_0.tiff.csv')
raw_data = pd.read_csv('data/Image_0006_0.tiff.csv', header=0)

data2 = raw_data[['X[mm]', 'Y[mm]', 'Z[mm]', 'Strain-global frame: Exx', 'Strain-global frame: Eyy']]
data2.to_csv('newcsvfile.csv', index=False)



for i in range(len(raw_data['X[mm]'])):
    print(raw_data['X[mm]'][i])
    pointstemp = [raw_data['X[mm]'][i], raw_data['Y[mm]'][i], raw_data['Z[mm]'][i]]
    points_csv.append(pointstemp)

meshcsv = pv.PolyData(points_csv, force_float = False)




#p.add_mesh(meshcsv)
p.add_mesh(meshcsv, scalars = raw_data['Strain-global frame: Eyy'])
 
points = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 

p.subplot(0,1)
mesh3 = pv.PolyData(points)


#plt.plot(xpoints, ypoints)
#plt.show()

p.add_mesh(mesh3)
p.show()