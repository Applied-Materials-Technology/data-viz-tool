from copier import Copier
import os
from pathlib import Path
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true")
parser.add_argument("--dev", action="store_true")

args = parser.parse_args()

if args.dev == False:
    data_loc = "data/csvs"
else:
    data_loc = "data/Data_viz"

print(args.dev)

#data_loc = "data/Data_viz"
#data_loc = "data/csvs"

if args.test == True:
    my_copier = Copier(os.path.join(Path.cwd().parent, data_loc), "example_inputloc")
else:
    my_copier = Copier(os.path.join(Path.cwd().parent, data_loc), os.path.join(Path.cwd().parent, "inputloc"))


my_copier.start()

