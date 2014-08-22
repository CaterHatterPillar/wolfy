#!/bin/python
# init.py
# Initialize a wolfy working directory.

import os
import sys
import argparse

import wolfy_util

argparser = argparse.ArgumentParser(prog='init', description=
                                    'Initialize a wolfy repository.')
args = argparser.parse_args(sys.argv[1:])

workDir = os.path.dirname(os.path.realpath(__file__))
wolfile = workDir + '/.wolfy'
if(os.path.isfile(wolfile)):
    print('wolfy working directory already initialized in: ' + workDir)
else:
    file = open(wolfile, 'w')
    file.write('# .wolfy\n'
               '# wolfy configuration file for Joe Dever\'s Lone Wolf series.\n'
               '# See https://github.com/CaterHatterPillar/wolfy\n'
               '# v. ' + wolfy_util.getVersionNumber() + '\n'
               '[wolfy]\n'
               '\nACTIVE_CHAR=NA\n')

    print('Created wolfy working directory in ' + workDir + '.\n'
          'Configure ' + wolfile + ' to modify wolfy behaviour.')
