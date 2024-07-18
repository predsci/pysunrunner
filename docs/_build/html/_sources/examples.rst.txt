Examples
========

Example #1: Sod
---------------

.. image:: _static/sod_1.png

.. code-block:: python

    import os
    import sys
    from numpy import *
    from matplotlib.pyplot import *
    import pyPLUTO as pypl
    import pyPLUTO.pload as pp

    plutodir = os.environ['PLUTO_DIR']
    wdir = plutodir+'/Test_Problems/HD/Sod/'
    nlinf = pypl.nlast_info(w_dir=wdir)

    D = pp.pload(nlinf['nlast'],w_dir=wdir) # Loading the data into a pload object D.

    f1 = figure()
    ax1 = f1.add_subplot(111)
    plot(D.x1,D.rho,'r',D.x1,D.prs,'k',D.x1,D.vx1,'g')
    xlabel(r'x')
    ylabel(r'$\rho$ [red], P [black], $V_{\rm x}$ [green]')
    title(r'Sod shock Tube test')
    axis([0.0,1.0,-0.2,1.2])
    savefig('sod_1.pdf')
    show()

Example #2: Rayleigh-Taylor
---------------------------

.. image:: _static/RayleighTaylor_multi.png

.. code-block:: python

    import os
    import sys
    from numpy import *
    from matplotlib.pyplot import *
    import pyPLUTO.pload as pp
    import pyPLUTO.Image as img

    plutodir = os.environ['PLUTO_DIR']
    wdir = plutodir+'/Test_Problems/MHD/Rayleigh_Taylor/'

    D0 = pp.pload(0,w_dir=wdir)
    D1 = pp.pload(1,w_dir=wdir) # Loading the data into a pload object D.
    D2 = pp.pload(2,w_dir=wdir)

    ## SMART WAY ##
    I = img.Image()
    I.multi_disp(D0.rho,D1.rho,D2.rho,x1=D0.x1,x2=D0.x2,Ncols=3,label1=3*['x'],
                 label2=3*['y'],title=[r'$\tau=0$',r'$\tau=1$',r'$\tau=2$'],
                 cbar=(True,'vertical','each'),figsize=[12,7])

    ## BRUTE FORCE WAY ##
    ## f1 = figure(figsize=[12,7])
    ## ax1 = f1.add_subplot(131)
    ## pcolormesh(D0.x1,D0.x2,D0.rho.T)
    ## colorbar()
    ## ax1.set_xlabel(r'x')
    ## ax1.set_ylabel(r'y')
    ## ax1.axis([-0.5,0.5,0.0,4.0])
    ## ax1.set_aspect('equal')
    ## ax1.set_title(r'$\tau$ = 0')

    ## ax2 = f1.add_subplot(132)
    ## pcolormesh(D1.x1,D1.x2,D1.rho.T)
    ## colorbar()
    ## ax2.set_xlabel(r'x')
    ## ax2.set_ylabel(r'y')
    ## ax2.axis([-0.5,0.5,0.0,4.0])
    ## ax2.set_aspect('equal')
    ## ax2.set_title(r'$\tau$ = 1')

    ## ax3 = f1.add_subplot(133)
    ## pcolormesh(D2.x1,D2.x2,D2.rho.T)
    ## colorbar()
    ## ax3.set_xlabel(r'x')
    ## ax3.set_ylabel(r'y')
    ## ax3.axis([-0.5,0.5,0.0,4.0])
    ## ax3.set_aspect('equal')
    ## ax3.set_title(r'$\tau$ = 2')

    savefig('RayleighTaylor_multi.png')
    show()

Example #3: Stellar-Wind
------------------------

.. image:: _static/stellar_wind.png

.. code-block:: python

    import os
    import sys
    from numpy import *
    from matplotlib.pyplot import *
    import pyPLUTO as pypl
    import pyPLUTO.pload as pp
    import pyPLUTO.Image as img
    import pyPLUTO.Tools as tl

    # To run this example [definitions_01.h] of Test_Problems/HD/Stellar_Wind
    # using pluto_01.ini and set the data in flt datatype.

    plutodir = os.environ['PLUTO_DIR']
    wdir = plutodir + '/Test_Problems/HD/Stellar_Wind/'
    nlinf = pypl.nlast_info(w_dir=wdir, datatype='flt')

    D = pp.pload(nlinf['nlast'], w_dir=wdir, datatype='flt')  # Loading the data into a pload object D.

    I = img.Image()
    I.pldisplay(D, log10(D.rho[:, 0, :]), x1=D.x1, x2=D.x3, label1='x', label2='y', 
                title=r'Log Density $\rho$ [Stellar Wind]', cbar=(True, 'vertical'), figsize=[8, 12])

    # Code to plot arrows. --> Spacing between the arrow can be adjusted by modifying the newdims tuple of conrid function.
    T = tl.Tools()
    newdims = 2 * (20,)
    Xmesh, Ymesh = meshgrid(D.x1.T, D.x3.T)
    xcong = T.congrid(Xmesh, newdims, method='linear')
    ycong = T.congrid(Ymesh, newdims, method='linear')
    velxcong = T.congrid(D.vx1[:, 0, :].T, newdims, method='linear')
    velycong = T.congrid(D.vx3[:, 0, :].T, newdims, method='linear')
    gca().quiver(xcong, ycong, velxcong, velycong, color='w')

    savefig('stellar_wind_1.png')
    show()

Example #4: Orzag-Tang
----------------------

.. image:: _static/orzag_tang_1.png

.. code-block:: python

    import os
    import sys
    from numpy import *
    from matplotlib.pyplot import *
    import pyPLUTO as pypl
    import pyPLUTO.pload as pp
    import pyPLUTO.Image as img

    plutodir = os.environ['PLUTO_DIR']
    wdir = plutodir + '/Test_Problems/MHD/Orszag_Tang/'
    nlinf = pypl.nlast_info(w_dir=wdir)

    D = pp.pload(nlinf['nlast'], w_dir=wdir)  # Loading the data into a pload object D.
    I = img.Image()
    I.pldisplay(D, D.rho, x1=D.x1, x2=D.x2, label1='x', label2='y', title=r'Density $\rho$ [Orszag Tang test]', cbar=(True, 'vertical'))
    savefig('Orszag_Tang.png')
    show()

Example #5: Spherical-Disc : FARGO
----------------------------------

.. image:: _static/SphDisk_1.png

.. code-block:: python

    import os
    import sys
    from numpy import *
    from matplotlib.pyplot import *
    import pyPLUTO as pypl
    import pyPLUTO.pload as pp
    import pyPLUTO.Image as img
    import pyPLUTO.Tools as tl

    plutodir = os.environ['PLUTO_DIR']
    wdir = plutodir+'/Test_Problems/MHD/FARGO/Spherical_Disk/'
    nlinf = pypl.nlast_info(w_dir=wdir, datatype='vtk')

    D = pp.pload(nlinf['nlast'], w_dir=wdir, datatype='vtk') # Loading the data into a pload object D.

    I = img.Image()

    f1 = figure(figsize=[15,6], num=1)
    ax1 = f1.add_subplot(122)
    I.pltSphData(D, w_dir=wdir, datatype='vtk', plvar='Bx1', logvar=False, rphi=False, x3cut=96)
    colorbar(orientation='horizontal')
    ax1.set_xlabel(r'Radius')
    ax1.set_ylabel(r'Height')
    ax1.set_title(r'Magnetic field $B_{\rm x}$')

    ax2 = f1.add_subplot(121)
    I.pltSphData(D, w_dir=wdir, datatype='vtk', plvar='rho', logvar=True, rphi=True, x2cut=24)
    colorbar(orientation='vertical')
    ax2.set_xlabel(r'x')
    ax2.set_ylabel(r'y')
    ax2.set_title(r'Log $\rho$')

    # Code to plot arrows. --> Spacing between the arrow can be adjusted by 
    # modifying the newdims tuple of conrid function.

    T = tl.Tools()
    newdims = 2*(20,)
    R, Z, SphData = I.getSphData(D, w_dir=wdir, datatype='vtk', rphi=True, x2cut=24)
    xcong = T.congrid(R, newdims, method='linear')
    ycong = T.congrid(Z, newdims, method='linear')
    vel1 = SphData['v1c']
    vel2 = SphData['v3c']

    xveccong = T.congrid(vel1, newdims, method='linear')
    yveccong = T.congrid(vel2, newdims, method='linear')
    normVp = sqrt(xveccong**2 + yveccong**2)
    xveccong = xveccong/normVp
    yveccong = yveccong/normVp
    ax2.quiver(xcong, ycong, xveccong, yveccong, color='w')

    show()

Example #6: X-point: Cosmic Rays Particles
------------------------------------------

.. image:: _static/xpoint_cr.png

.. code-block:: python

    import os
    import pyPLUTO as pypl
    import pyPLUTO.pload as pp
    import pyPLUTO.ploadparticles as pr
    import matplotlib.pyplot as plt
    import numpy as np

    plutodir = os.environ['PLUTO_DIR']
    wdir = plutodir+'/Test_Problems/Particles/CR/Xpoint/'
    nlinf = pypl.nlast_info(w_dir=wdir, datatype='flt')

    D = pp.pload(nlinf['nlast'], w_dir=wdir, datatype='flt')
    P = pr.ploadparticles(nlinf['nlast'], w_dir=wdir, datatype='flt')

    Bmag = D.Bx1**2 + D.Bx2**2
    f1 = plt.figure(figsize=[8,8])
    im0 = plt.imshow(Bmag.T, origin='image', extent=[D.x1.min(), D.x1.max(), D.x2.min(), D.x2.max()])
    plt.colorbar(im0)
    plt.xlabel(r'X-axis')
    plt.ylabel(r'Y-axis')
    plt.title(r'Magnetic Energy [X-point test] with Scatter Plot of Highenergy CR particles', fontsize=12)
    p_eng = 0.5 * (P.vx1**2 + P.vx2**2)
    indx_sort = p_eng.argsort()
    x1s, x2s, pengs = P.x1[indx_sort], P.x2[indx_sort], p_eng[indx_sort]
    im1 = plt.scatter(x1s[-3000:], x2s[-3000:], s=10, c=pengs[-3000:], cmap='copper', alpha=0.7)
    plt.colorbar(im1, orientation='horizontal')
    plt.minorticks_on()
    plt.savefig('xpoint_cr.png')

Example #7: Planar Shock: Lagrangian Particles
----------------------------------------------

.. image:: _static/plnshk_1.png

.. code-block:: python

    import os
    import sys
    from numpy import *
    from matplotlib.pyplot import *
    import pyPLUTO as pypl
    import pyPLUTO.pload as pp
    import pyPLUTO.Image as img
    import pyPLUTO.Tools as tl

    plutodir = os.environ['PLUTO_DIR']
    wdir = plutodir + '/Test_Problems/MHD/FARGO/Spherical_Disk/'
    nlinf = pypl.nlast_info(w_dir=wdir, datatype='vtk')

    D = pp.pload(nlinf['nlast'], w_dir=wdir, datatype='vtk')  # Loading the data into a pload object D.

    I = img.Image()

    f1 = figure(figsize=[15, 6], num=1)
    ax1 = f1.add_subplot(122)
    I.pltSphData(D, w_dir=wdir, datatype='vtk', plvar='Bx1', logvar=False, rphi=False, x3cut=96)
    colorbar(orientation='horizontal')
    ax1.set_xlabel(r'Radius')
    ax1.set_ylabel(r'Height')
    ax1.set_title(r'Magnetic field $B_{\rm x}$')

    ax2 = f1.add_subplot(121)
    I.pltSphData(D, w_dir=wdir, datatype='vtk', plvar='rho', logvar=True, rphi=True, x2cut=24)
    colorbar(orientation='vertical')
    ax2.set_xlabel(r'x')
    ax2.set_ylabel(r'y')
    ax2.set_title(r'Log $\rho$')

    # Code to plot arrows. --> Spacing between the arrow can be adjusted by
    # modifying the newdims tuple of conrid function.

    T = tl.Tools()
    newdims = 2 * (20,)
    R, Z, SphData = I.getSphData(D, w_dir=wdir, datatype='vtk', rphi=True, x2cut=24)
    xcong = T.congrid(R, newdims, method='linear')
    ycong = T.congrid(Z, newdims, method='linear')
    vel1 = SphData['v1c']
    vel2 = SphData['v3c']

    xveccong = T.congrid(vel1, newdims, method='linear')
    yveccong = T.congrid(vel2, newdims, method='linear')
    normVp = sqrt(xveccong**2 + yveccong**2)
    xveccong = xveccong / normVp
    yveccong = yveccong / normVp
    ax2.quiver(xcong, ycong, xveccong, yveccong, color='w')

    show()
