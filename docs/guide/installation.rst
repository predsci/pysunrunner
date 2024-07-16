Installation
============

The current version of SRPy has been updated to support Python version 3 and is tested with > 3.6.

Global Install
--------------
The Python version from the EPD version by default creates a PYTHONPATH. 
If no option is chosen for preferred path then in that case the code will be installed in that default path. 
This may require the user to have access to the root password:
Enter into the directory : cd $PLUTO_DIR/Tools/pyPLUTO
Install the code in the default path: python setup.py install

Local Install 
-------------
The best practice is to create your own PYTHONPATH and do a local install in the following way:
  * Create a directory where to store this module : mkdir MyPython_Modules
  * Enter into the directory : cd $PLUTO_DIR/Tools/pyPLUTO
  * Install the code in the directory created : python setup.py install --prefix=<path to MyPython_Modules>
  * Then append the following in your .bashrc :
  * export PYTHONPATH =<path to MyPython_Modules>/lib/python<ver>/site-packages
  * export PATH =<path to MyPython_Modules>/bin:$PATH

where <ver> is the python version which the user have used to install the package.