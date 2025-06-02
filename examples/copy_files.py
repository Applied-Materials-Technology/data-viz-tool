from copier import Copier
import os
from pathlib import Path
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true")

args = parser.parse_args()

if args.test == True:
    my_copier = Copier(os.path.join(Path.cwd().parent, "data/Data_viz"), "example_inputloc")
else:
    my_copier = Copier(os.path.join(Path.cwd().parent, "data/Data_viz"), os.path.join(Path.cwd().parent, "inputloc"))

my_copier.start()

