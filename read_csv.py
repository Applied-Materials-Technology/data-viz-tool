import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#pv.set_plot_theme(pv.themes.ParaViewTheme())

p = pv.Plotter(shape=(1,2))
#p = pv.Plotter()
p.subplot(0, 0)
#mesh1 = pv.read('data/stc-thermomech-basic-bcbase_out.e')
#mesh1 = pv.PolyData('data/Image_0006_0.tiff.csv')
raw_data = pd.read_csv('data/Image_0006_0.tiff.csv', header=0, comment="#",
                       delim_whitespace=True, names=["X[mm]", "Y[mm]", "Z[mm]"])


loc = raw_data[raw_data.columns[1:4]]
points_3d = loc.to_numpy()
#cloud = pv.PolyData(points_3d)
#surf = cloud.delaunay_2d()
#surf.plot(show_edges=True)

#vertices = raw_data.iloc[vidxs][["X[mm]", "Y[mm]", "Z[mm]"]].values
mesh1 = pv.PolyData(points_3d)

#mesh2 = pv.PolyData(points)
p.add_mesh(mesh1, show_edges=False)

p.add_mesh(mesh1, show_edges=False)


#p.subplot(0,3)
#xpoints = np.array([0, 6])
#ypoints = np.array([0, 250])
#zpoints = np.array([0,0])
 
points = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 

p.subplot(0,1)
mesh3 = pv.PolyData(points)


#plt.plot(xpoints, ypoints)
#plt.show()

p.add_mesh(mesh3)
p.show()