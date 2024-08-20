import os
import sys
import pysunrunner
import pysunrunner.pload as pp
import pysunrunner.io as io
import pysunrunner.pviz as pviz

import numpy as np
import matplotlib.pyplot as plt


# name of variable that will be plotted
var_name = 'vx1'

# Path to the directory containing PLUTO output files
# Update this path to your specific location
pluto_path = "/path/to/location/of/pluto/output/"

wdir = pluto_path

# Read time information from the output directory (in PLUTO units)
time = io.read_time(w_dir=wdir, datatype='dbl')
time = np.array(time, dtype=np.float32)

# Convert time from PLUTO units to hours 
# Time conversion factor: PLUTO units to hours
time_fac_pluto = 1.49597871e+08 / 3600
time_h = time * time_fac_pluto

# Dimension for stack plot (can be 'r', 't', or 'p')
# In this case, the stack plot is for 1-D cuts in the phi dimension
stack_dim = 'p'

# Radial distance (in AU) for the stack plot
r_val = 1.0 

# Latitude value for the stack plot, set to equatorial (0 degrees)
t_val = np.deg2rad(0.0)

# Retrieve variable from the PLUTO output
print('Retrieving variable. This may take some time..')

# Find out how many PLUTO dumps we have
nlinf = io.nlast_info(w_dir=wdir, datatype='dbl')
nlast = nlinf['nlast']

# Initialize an empty list to store PLUTO data
pluto_list = []

# Loop through all output files and append the data to pluto_list
for ii in range(0, nlast):
	D = pp.pload(ii,w_dir=wdir,datatype='dbl')
	pluto_list.append(D)


# Set phi-values for the stack plot
# This is an advanced example: the phi slices will be plotted at a series of equi-spaced phi values,
# using periodic boundary conditions.

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

# Determine the phi values corresponding to the indices
phi_cut = p_coords[i_phi_slice]

# End of phi slice calculation

# X and Y axes labels
xlabel = 'Time (hours)'
ylabel = ''

# Plot title (set to None if not needed)
title = None

# Color scheme for the plot
cmap = 'rainbow'

# Y-axis shift value for the stack plot
yshift = 1200


# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Generate the stack plot using the specified parameters
ax = pviz.plot_stack(pluto_list=pluto_list, var_name = var_name,
        r_val = r_val, t_val=t_val, p_val=phi_cut, stack_dim = stack_dim, time = time_h, ax=ax, cmap = cmap,
        title = title, xlabel = xlabel, ylabel = ylabel, log_scale = False, yshift = yshift)

# Save the plot to a file
file_name = var_name + '_1D_stack_plot.png'
plt.savefig(file_name, dpi=150)

# to plot to screen uncomment the line below
#plt.show()

