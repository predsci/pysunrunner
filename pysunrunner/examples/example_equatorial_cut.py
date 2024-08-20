import os
import sys
import pysunrunner
import pysunrunner.pload as pp
import pysunrunner.io as io
import pysunrunner.pviz as pviz

import numpy as np
import matplotlib.pyplot as plt

# Variable to be plotted
var_name = 'vx1'

# Path to the directory containing PLUTO output files
pluto_path = "/path/to/location/of/pluto/output/"

wdir = pluto_path

# Read time information from the output directory (in PLUTO units)
time = io.read_time(w_dir=wdir, datatype='dbl')
time = np.array(time, dtype=np.float32)

# Convert time from PLUTO units to hours (time factor: PLUTO units to hours)
time_fac_pluto = 1.49597871e+08 / 3600
time_h = time * time_fac_pluto

# Set the time point index to be plotted
time_idx = 42

# Load PLUTO simulation results for the specified time point
D = pp.pload(time_idx, w_dir=wdir, datatype='dbl')

# Set polar projection for the plot
subplot_kw = {'projection': "polar"}

# Set color map for the plot (default is 'rainbow')
cmap = 'rainbow'

# Set title for the plot
title = 'Radial Velocity'

# Set minimum and maximum values for the z-scale (color scale).
# These are optional; if not set, the min/max values in the data will be used.
zmin = 200
zmax = 2200

# Set log_scale to True for a log10 plot of the data (useful for variables like pressure)
log_scale = False

# Set r_scale to True to apply r^2 scaling (useful for variables like scaled radial magnetic field or density)
r_scale = False

# Create a figure with a single subplot using polar projection
fig, ax = plt.subplots(subplot_kw=subplot_kw, figsize=(5, 5))

# Plot the equatorial cut of the data on the polar projection
axs = pviz.plot_equatorial_cut(D=D, var_name=var_name, ax=ax, cmap=cmap, title=title,
                               r_scale=r_scale, log_scale=log_scale, zmin=zmin, zmax=zmax)

# Save the plot to a PNG file with a descriptive filename
file_name = var_name + '_equi_cut_time_index=' + str(time_idx) + '.png'
plt.savefig(file_name, dpi=150)

# To display the plot on the screen, uncomment the line below
# plt.show()



