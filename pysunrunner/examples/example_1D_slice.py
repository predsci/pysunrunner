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

time = io.read_time(w_dir=wdir,datatype='dbl')
time = np.array(time, dtype=np.float32)


# Load PLUTO simulation results for the specified time point
D = pp.pload(time_idx, w_dir=wdir, datatype='dbl')

# Plot is made as a function of radial distance, hence r_cut is set to None
r_cut = None

# Plot is made at theta == equatorial
theta_cut = np.deg2rad(0.0)

# Phi slices will be plotted at a series of equi-spaced phi values,
# using periodic boundary conditions.
# This is an advanced example.

# Retrieve the phi grid from the PLUTO data structure
p_coords = np.array(D.x3)

# Define phi slice indices (e.g., 18 equi-spaced slices)
i_phi_slice = 250 + 5*np.arange(18)

# Number of phi slices
n_slice = len(i_phi_slice)

# Adjust phi slice indices to stay within the bounds of the phi grid
for ii in range(0, n_slice):
    if (i_phi_slice[ii] >= len(p_coords)):
        i_phi_slice[ii] = i_phi_slice[ii] - len(p_coords)

# Determine the phi values corresponding to the adjusted slice indices
phi_cut = p_coords[i_phi_slice]

# End of phi slice calculation

# Plot color scheme
cmap = 'rainbow'

# Plot title (with formatted theta value)
title = 'Radial velocity as a function of heliocentric distance, theta = '+str(round(np.rad2deg(theta_cut),1))

# Y-axis limits (optional; if not set, min/max values in the data will be used)
ymin = 0.0
ymax = 2500.00 

# X and Y axes labels
xlabel = 'R (AU)' # R is the radial distance in Astronomical Units (AU)
ylabel = 'V (km s$^{-1}$)' # V is the velocity in km/s

# Create a figure with a single subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the slices with the specified parameters
axs = pviz.plot_slice(D=D, var_name = var_name,
        r_cut=r_cut, theta_cut=theta_cut, phi_cut=phi_cut, ax=ax, cmap = cmap, 
        title = title, xlabel = xlabel, ylabel = ylabel, ymin = ymin, ymax = ymax)

# Save the plot to a PNG file with a descriptive filename
file_name = var_name + '_1d_cut_theta=' + str(round(np.rad2deg(theta_cut),1)) + '.png'
plt.savefig(file_name, dpi=150)

# to plot to screen uncomment the line below
#plt.show()


