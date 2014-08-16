#!/bin/python
# init.py
# Initialize a wolfy working directory.

import os

workDir = os.path.dirname(os.path.realpath(__file__))
wolfile = workDir + "/.wolfy"
if(os.path.isfile(wolfile)):
    print("wolfy working directory already initialized in: " + workdir)
else:
    file = open(wolfile, 'w')
    file.write("# " + ".wolfy\n"
               "# wolfy configuration file for Joe Dever's Lone Wolf series.\n"
               "# See https://github.com/CaterHatterPillar/wolfy\n#\n"
               "\nACTIVE_CHAR NA\n")

    print("Created wolfy working directory in " + workDir +
          ". Configure " + wolfile + " to modify wolfy behaviour.")
