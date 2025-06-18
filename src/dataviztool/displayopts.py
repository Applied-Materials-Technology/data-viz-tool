from __future__ import annotations
import numpy as np
import pyvista as pv
from dataclasses import dataclass

@dataclass(slots=True)
class DisplayOpts:
    """
    Dataclass for pyvista plotting settings
    """

    """
    The colour map from the selection of valid matplotlib colour maps
    """
    colourmap: str = 'viridis'

    """
    plt.get_cmap luv
    """

    colour_divs: int = 10