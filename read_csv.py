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
raw_data = pd.read_csv('data/Image_0006_0.tiff.csv', header=0)

data2 = raw_data[['X[mm]', 'Y[mm]', 'Z[mm]']]
data2.to_csv('newcsvfile.csv', index=False)

print(raw_data['X[mm]'])

for i in range(len(raw_data['X[mm]'])):
    print(i)

#mesh1 = pv.PolyData(raw_data)

#mesh2 = pv.PolyData(points)
#p.add_mesh(mesh1, show_edges=False)




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