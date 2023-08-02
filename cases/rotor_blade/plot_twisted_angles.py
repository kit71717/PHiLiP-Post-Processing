#-----------------------------------------------------
# Import public libraries
import numpy as np # NumPy: contains basic numerical routines
import scipy # SciPy: contains additional numerical routines to numpy
#-----------------------------------------------------
# Import personal libraries
import os;CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]+"/";
import sys
sys.path.append(CURRENT_PATH+"../../submodules/quickplotlib/lib"); import quickplotlib as qp
#-----------------------------------------------------
x_store = []
y_store = []
labels_store = []

filename="blade_geo.dat"

# set 1
x,y = np.loadtxt(filename,usecols=(3,1),unpack=True)
x_store.append(x)
y_store.append(y)
labels_store.append("Design Cycle 1")
# set 2
x,y = np.loadtxt(filename,usecols=(3,4),unpack=True)
x_store.append(x)
y_store.append(y)
labels_store.append("Design Cycle 2")
# set 3
x,y = np.loadtxt(filename,usecols=(3,5),unpack=True)
x_store.append(x)
y_store.append(y)
labels_store.append("Design Cycle 3")

qp.plotfxn(x_store,y_store,
    figure_filename="twisted_angles",
    figure_size=(9,6),
    legend_labels_tex=labels_store,
    figure_filetype="pdf",
    title_label="Spanwise Position from Tip to Root vs Twisted Angle",
    ylabel="Twisted Angle [$^{\\circ}$]",
    xlabel="Spanwise Position [mm]",
    xlimits=[0,230],
    transparent_legend=False,
    legend_border_on=True,
    grid_lines_on=False)