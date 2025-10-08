[](https://github.com/Applied-Materials-Technology/data-viz-tool/tree/dev#data-viz-tool)

A python tool for visualising live data.

## Installation:

### Virtual Environment

We recommend installing in a virtual environment using `venv`:

```
python -m venv dataviz-env
source dataviz-env/bin/activate
```

### Standard Installation

Clone to your local system and `cd` to the root directory of `dataviztool`. Ensure you virtual environment is activated and run from the `dataviztool` root directory:

```
pip install .
```

### Developer Installation

To create an editable installation, follow the instructions for a standard installation but run:

```
pip install -e .
```

Pycdata can be used to generate data for testing purposes. It can be found here [https://github.com/Applied-Materials-Technology/pycdata](https://github.com/Applied-Materials-Technology/pycdata)

## Getting Started
###### Run example:
Note: example requires running code in two different terminals
Within the examples directory, ex1_show_side_compare.py contains the set up for the displayer, and copy_files.py triggers the the simulation of files being delivered to the tracked directory.

In terminal 1
```
python ex1_show_side_compare.py
```

In terminal 2
```
python copy_files.py --test
```

###### To set up plotter manually...
See examples/ex3_manual_plotter.py for example.

Set up displayer opts (can skip if using defaults)
```python
displayopts = DisplayerOpts()
#if reading csvs
displayopts.set_csv_coords(x_coordinate, y_coordinate, z_coordinate, field)
```

Create displayer and subplots
```python
my_displayer = Displayer(automake_plotter=False, watch_path = "example_inputloc", display_opts=displayopts)
my_displayer.create_plotter(1,2)
my_displayer.assign_subplot(0,0,"Subplot heading", "Name of folder to read data")
my_displayer.assign_subplot(0,1,"Subplot heading", "Name of folder to read data")
```

Start watcher and wait for data arrival
```python
my_watcher = Watcher(displayer = my_displayer, watch_path="path/to/incoming/data")
my_watcher.run()
```


