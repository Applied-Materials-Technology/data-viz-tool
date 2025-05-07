# data-viz-tool


1. pip install -r requirements.txt
     - pycdata is recommended to generate data for this test. It can be found here https://github.com/Applied-Materials-Technology/pycdata

2. To display generated data
     - If using pycdata to generate data, you can run examples/ex1_generate_data.py to start generation of test data
     - For a single display, run src/dataviztool/dataviztool.py
     - Specify the directory that will be tracked with watchDirectory in src/dataviztool/dataviztool.py.py (default: watchDirectory = Path("example_generate")) 
     - For a single display csv version, run src/dataviztool/main_csv.py. 
     - For a side-by-side display run src/dataviztool/double_view.py. Input location of data should be inputloc/left (for left display) and inputloc/right (for right display)

3. Example:
     - Note: example requires running code in two different terminals
     - within the examples directory, ex1_show_side_compare.py contains the set up for the displayer, and copy_files.py triggers the the simulation of files being 
       delivered to the tracked directory