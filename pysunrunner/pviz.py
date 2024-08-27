import numpy as np
import matplotlib.pyplot as plt

def plot_equatorial_cut(D, ax, var_name = 'vx1', cmap = None, title = None, r_scale = False, log_scale = False, 
    zmin = None, zmax = None, conversion_units = None):
    """
    Function to plot the equatorial cut.

    Parameters:
    D: PLUTO 3D array of data values
    var_name: variable to plot
    cmap: colormap name
    title: plot title
    r_scale (logical): if True scaled data is plotted (x R^2)
    log_scale (logical): if True log10 of data is plotted
    zmin (scalar): Minimum value for color scaling
    zmax (scalar): Maximum value for color scaling
    conversion_units (scalar): factor to convert units. If None, no conversion 
    **Outputs**:
    ax: subplot with equitorial cut of data
    """

    if cmap is None:
        cmap = 'rainbow'
 
    if title is None:
        title = ''
    if conversion_units is None:
        conversion_units = 1.0

    # the coordinates are D.x1 D.x2 and D.x3 (r, theta, phi)
    r_coords = np.array(D.x1)
    t_coords = np.array(D.x2)
    p_coords = np.array(D.x3)
    
    # Convert from co-latitude to latitude
    t_coords = np.pi/2 - t_coords

    # retrieve the data to be plotted
    data = getattr(D, var_name)

    if zmin is None:
        zmin = np.min(data) 
    if zmax is None:
        zmax = np.max(data)

    # convert units 
    data = data * conversion_units
    zmin = zmin * conversion_units
    zmax = zmax * conversion_units

    # calculate R^2
    if (r_scale):
        r2_coords = np.multiply(r_coords, r_coords)

    # Create a meshgrid for spherical coordinates
    phi_grid, r_grid = np.meshgrid(p_coords, r_coords)

    # Find the index where theta is closest to 0 (equatorial plane)

    theta_equatorial_index = np.argmin(np.abs(t_coords - 0))

    tmp = data[:,theta_equatorial_index,:]

    # Transpose
    tmp = tmp.T

    if r_scale:
        tmp = np.multiply(tmp, r2_coords)

    if log_scale:
        tmp = np.log10(tmp)    

    Z = tmp.T
    c = ax.pcolormesh(phi_grid, r_grid, Z, shading='auto', cmap=cmap, vmin = zmin, vmax = zmax)
    ax.set_title(title)
    ax.grid(True, axis ='y')  # show R grid
    ax.grid(False, axis ='x')  # Remove angle grid
    ax.set_ylim(0, np.max(r_coords))
    # ax.set_yticks([]) # remove the R labels  (remove line if we want to keep it)    
    colorbar = plt.colorbar(c, ax=ax, orientation='horizontal', shrink = 0.5, aspect = 20)
   #colorbar.set_label(cbar_label, fontsize=12)  # To add label for color bar
    return ax


def plot_phi_cut(D, ax, var_name = 'vx1', phi_cut = np.pi, cmap = None, title = None, 
    r_scale = False, log_scale = False, zmin = None, zmax = None, conversion_units = None):
    """
    Function to plot phi cut.

    Parameters:
    D: PLUTO 3D array of data values.
    var_name: variable to plot
    phi_cut: angle in radians for phi_cut, default is meridonial
    cmap: colormap name
    title: plot title
    r_scale (logical): if True scaled data is plotted (x R^2)
    log_scale (logical): if True log10 of data is plotted
    zmin (scalar): Minimum value for color scaling
    zmax (scalar): Maximum value for color scaling
    conversion_units (scalar): factor to convert units.  If None, no conversion 

    **Outputs**:
    ax: subplot with phi cut of data
    """

    if cmap is None:
        cmap = 'rainbow'

    if title is None:
        title = ''
    if conversion_units is None:
        conversion_units = 1.0


    # the coordinates are D.x1 D.x2 and D.x3 (r, theta, phi)
    r_coords = np.array(D.x1)
    t_coords = np.array(D.x2)
    p_coords = np.array(D.x3)
    # Convert from co-latitude to latitude
    t_coords = np.pi/2 - t_coords

    #Extract data for plotting

    data = getattr(D, var_name)



    # calculate R^2
    if (r_scale):
        r2_coords = np.multiply(r_coords, r_coords)

    # Create a meshgrid for theta and R
    t_grid, r_grid = np.meshgrid(t_coords, r_coords)

    # Find the index where phi is closest to phi_cut

    phi_index = np.argmin(np.abs(p_coords - phi_cut))

    tmp = data[:,:,phi_index]

    if zmin is None:
        zmin = np.min(tmp)
    if zmax is None:
        zmax = np.max(tmp)

    # convert units 
    data = tmp * conversion_units
    zmin = zmin * conversion_units
    zmax = zmax * conversion_units

    # Transpose
    tmp = tmp.T

    if r_scale:
        tmp = np.multiply(tmp, r2_coords)

    if log_scale:
        tmp = np.log10(tmp)    

    Z = tmp.T
    c = ax.pcolormesh(t_grid, r_grid, Z, shading='auto', cmap=cmap, vmin = zmin, vmax = zmax)
    ax.set_title(title)
    ax.grid(False)
    ax.set_thetalim(-np.pi / 2, np.pi / 2)
    ax.set_xticks([-np.pi/2, -np.pi/4,0,np.pi/4,np.pi/2])
    colorbar = plt.colorbar(c, ax=ax, orientation='horizontal', shrink = 0.5, aspect = 20, pad = 0.1)

    return ax

def plot_slice(D, ax, var_name = 'vx1', r_cut = None, theta_cut = 0.0, phi_cut = np.pi, cmap = None, title = None, 
    xlabel = 'R (AU)', ylabel = 'V (km s$^{s-1}$)', r_scale = False, log_scale = False, ymin = None, ymax = None,
    conversion_units = None):
    """
    Function to plot 1-D slices

    Parameters:
    D: PLUTO 3D array of data values.
    var_name: variable name for plotting
    r_cut: distance in AU for an r-cut, if None data plotted as a function of r
    theta_cut: latitude angle in radians for a theta-cut, default is equatorial, if None cuts are plotted as a function of theta
    phi_cut: angle in radians for phi-cut, default is meridonial, if None cuts are plotted as a function of phi
    cmap: colormap name
    title: plot title
    xlabel: x-axis label
    ylabel: y-axis label
    r_scale (logical): if True scaled data is plotted (x R^2)
    log_scale (logical): if True log10 of data is plotted
    ymin (scalar): Minimum y-axis value for plot
    ymax (scalar): Maximum y-axis value for plot
    conversion_units (scalar): factor to convert units.  If None, no conversion

    **Outputs**:
    ax: A plot with one or more slices
    """

    if cmap is None:
        cmap = 'rainbow'

    if title is None:
        title = ''
    
    if xlabel is None:
        xlabel = 'x-axis'

    if ylabel is None:
        ylabel = 'y-axis'

    if conversion_units is None:
        conversion_units = 1.0

    # the coordinates are D.x1 D.x2 and D.x3 (r, theta, phi)
    r_coords = np.array(D.x1)
    t_coords = np.array(D.x2)
    p_coords = np.array(D.x3)

    # Convert from co-latitude to latitude
    t_coords = np.pi/2 - t_coords
    
    # Extract the vx1 data 
    data = getattr(D, var_name)

    # determine what each dimension of r, t, p is (i.e., what is the x-axis for the plot which dimension)    
    if r_cut is None:
        theta_cut = np.array(theta_cut)
        phi_cut = np.array(phi_cut)
        theta_cut = np.atleast_1d(theta_cut)
        phi_cut = np.atleast_1d(phi_cut)
        slice_dim = 1
        if len(theta_cut) == 1:
            theta_index = np.argmin(np.abs(t_coords - theta_cut))
            data_2d = data[:,theta_index,:]
            slice_index = np.array([np.argmin(np.abs(p_coords - phi)) for phi in phi_cut])
            slice_val = p_coords[slice_index]
        else:
            phi_index = np.argmin(np.abs(p_coords - phi_cut))
            data_2d = data[:,:,phi_index]
            slice_index = np.array([np.argmin(np.abs(t_coords - theta)) for theta in theta_cut])
            slice_val = t_coords[slice_index]

        label = np.round(np.rad2deg(slice_val)).astype(int)
        x = r_coords

    if theta_cut is None:
        r_cut = np.array(r_cut)
        phi_cut = np.array(phi_cut)
        r_cut = np.atleast_1d(r_cut)
        phi_cut = np.atleast_1d(phi_cut)   
        if len(r_cut) == 1:
            r_index = np.argmin(np.abs(r_coords - r_cut))
            data_2d = data[r_index,:,:]
            slice_index = np.array([np.argmin(np.abs(p_coords - phi)) for phi in phi_cut])
            slice_dim = 1
            slice_val = p_coords[slice_index]
            label = np.round(np.rad2deg(slice_val)).astype(int)
        else:
            phi_index = np.argmin(np.abs(p_coords - phi_cut))
            data_2d = data[:,:,phi_index]
            slice_index = np.array([np.argmin(np.abs(r_coords - r)) for r in r_cut])
            slice_dim = 0
            slice_val = r_coords[slice_index]
            label = np.round(slice_val).astype(int)

        x = t_coords

    if phi_cut is None:
        r_cut = np.array(r_cut)
        theta_cut = np.array(theta_cut)
        r_cut = np.atleast_1d(r_cut)
        theta_cut = np.atleast_1d(theta_cut)
        slice_dim = 0    
        if len(r_cut) == 1:
            r_index = np.argmin(np.abs(r_coords - r_cut))
            data_2d = data[r_index,:,:]
            slice_index = np.array([np.argmin(np.abs(t_coords - theta)) for theta in theta_cut])
            slice_val = t_coords[slice_index]
            label = np.round(np.rad2deg(slice_val)).astype(int)
        else:
            theta_index = np.argmin(np.abs(t_coords - theta_cut))
            data_2d = data[:,theta_index,:]
            slice_index = np.array([np.argmin(np.abs(r_coords - r)) for r in r_cut])
            slice_val = r_coords[slice_index]
            label = np.round(slice_val).astype(int)

        x = p_coords


    if ymin is None:
        ymin = np.min(data_2d)
    if ymax is None:
        ymax = np.max(data_2d)

   # convert units
    data_2d = data_2d * conversion_units
    ymin = ymin * conversion_units
    ymax = ymax * conversion_units

    n_slice = len(slice_index)
    indices = np.linspace(0, 1, n_slice)
    # cmap = plt.colormaps[cmap]
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(indices)

 
    # calculate R^2
    if r_scale:
        r2_coords = np.multiply(r_coords, r_coords)

    if log_scale:
        data_2d = np.log10(data_2d)

    jcount = 0
    if slice_dim == 1:
        for islice in slice_index:
            y = data_2d[:,islice]
            ax.plot(x, y, color = colors[jcount], label = label[jcount])
            jcount = jcount + 1

    jcount = 0
    if slice_dim == 0:
        for islice in slice_index:
            y = data_2d[islice,:]
            if r_scale:
                y = np.multiply(y, r2_coords)
            ax.plot(x, y, color = colors[jcount], label = label[jcount])
            jcount = jcount + 1

    #Set ymin and ymax
    plt.ylim(ymin, ymax)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)  # Change '14' to the desired size
    plt.legend()

    return ax

def plot_stack(pluto_list, ax, var_name = 'vx1', r_val = 1.0, t_val = 0.0, p_val=np.pi, stack_dim = 'p', time= None, 
    cmap = None, title = None, 
    xlabel = 'Time [hours]', ylabel = '', log_scale = False, yshift=None):
    """
    Function For a 1-D stack plot
    Parameters:
    pluto_list: A list with each item a PLUTO 3D array of data values
    var_name: variable name for plotting
    r_val: distance (in AU) for cut
    t_val: latitude (in radians) for cut
    p_val: longitude (in radians) for 
    stack_dim: dimension for the stack plot (r, t, or p)
    time: time array (units are hours)
    cmap: colormap name
    title: plot title
    xlabel: x-axis label
    ylabel: y-axis label
    r_scale (logical): if True scaled data is plotted (x R^2)
    log_scale (logical): if True log10 of data is plotted

    **Outputs**:
    ax: A plot with one or more slices
    """


    if yshift is None:
        yshift = 0.0

    if xlabel is None:
        xlabel = 'x-axis'
    if ylabel is None:
        ylabel = 'y-axis'

    # retrieve the first element in the list so we can retrieve the coordinates
    D = pluto_list[0]


    # the coordinates are D.x1 D.x2 and D.x3 (r, theta, phi)
    r_coords = np.array(D.x1)
    t_coords = np.array(D.x2)
    p_coords = np.array(D.x3)
    # convert t_coords wfrom co-latitude to latitude

    t_coords = np.pi/2 - t_coords

    # Number of time steps/elemts in the pluto_list

    ntimes = len(pluto_list)

    # find the r_index for the plot
    if stack_dim != 'r':
        r_idx = np.argmin(np.abs(r_coords- r_val))
    else:
        n_slice = len(r_val)
        r_idx = np.zeros(n_slice, dtype=int)
        labels = np.zeros(n_slice, dtype=int)
        icount = 0
        for r_slice in r_val:
            r_idx[icount] = np.argmin(np.abs(r_coords - r_slice))
            labels[icount] = np.round(p_coords[p_idx[icount]]).astype(int)
            icount = icount + 1

    # repeat for t_index
    if stack_dim != 't':
        t_idx = np.argmin(np.abs(t_coords - t_val))
    else:
        n_slice = len(t_val)
        t_idx = np.zeros(n_slice, dtype=int)
        labels = np.zeros(n_slice, dtype=int)
        icount = 0
        for th_slice in t_val:
            t_idx[icount] = np.argmin(np.abs(t_coords - th_slice))
            labels[icount] = np.round(np.rad2deg(t_coords[t_idx[icount]])).astype(int)
            icount = icount + 1

    # and for p_index:
    if stack_dim != 'p':
        p_idx = np.argmin(np.abs(p_coords - p_val))
    else: 
        n_slice = len(p_val)
        p_idx = np.zeros(n_slice, dtype=int)
        labels = np.zeros(n_slice, dtype=int)
        icount = 0
        for fi_slice in p_val:
            p_idx[icount] = np.argmin(np.abs(p_coords - fi_slice))
            labels[icount] = np.round(np.rad2deg(p_coords[p_idx[icount]])).astype(int)
            icount = icount + 1

    array_2d = np.zeros((n_slice, ntimes))
    
    for ii in range(0, ntimes):
        D = pluto_list[ii]
        data = getattr(D, var_name)
        array_2d[:,ii] = data[r_idx, t_idx,p_idx]
        
    if log_scale:
        array_2d = np.log10(array_2d)

    # remove all time elements prior to the CME launch
    
    time = [x for x in time if x >= 0]

    #cmap = plt.colormaps[cmap]
    cmap = plt.cm.get_cmap('rainbow')
    indices = np.linspace(0, 1, n_slice)
    colors = cmap(indices)

    # location for vertical line

    x_value = 10
    y1 = 2000
    y2 = y1 * 2

    for ii in range(0, n_slice):
        tmp = array_2d[ii,:] + yshift * ii
        ax.plot(time, tmp, color=colors[ii], linestyle='-', linewidth=1, label = labels[ii]) 
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(np.min(time),np.max(time)) # limit xrange to be 0-40 hours
    plt.gca().set_yticklabels([]) # remove y-ticks labels for stack plot
    plt.vlines(x=x_value, ymin=y1, ymax=y2, colors='black', linewidth=2)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)  # Change '14' to the desired size
    plt.legend(loc='center left', bbox_to_anchor=(0.8, 0.5))
    # plt.legend()

    return ax


