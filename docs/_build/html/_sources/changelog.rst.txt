ChangeLog
=========

This is the initial release of srpy (standing for sunRunner-Python): version 0.1

The following are changes in the pyPLUTO code which forms the basis for srpy3d: 

CHANGES from 4-1.0 to 4-2.0:

1. The files have now been modified to support Python version >3.6.
The version for Python 2.7.x has now become obsolete will not be supported hence forth.

2. The datareader now treats each of the reader and associated functionality as a different class, this results in slight 
change of the syntax with regard to import of pload module. 
Example : To read say data.0030.dbl, we have to do. 

import pyPLUTO.pload as pp
D = pp.pload(30)

instead of in the older version

import pyPLUTO as pp
D = pp.pload(30) 

3. The Reader also has support to read particle files that are generated using the 
newly developed Hybrid Eulerian Lagrangian Framework.
