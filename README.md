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



