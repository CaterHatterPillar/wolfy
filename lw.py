#!/bin/python
# lw.py
# Create a Lone Wolf character.

# System errors:
# 1 - Erronous arguments given.
# 2 - Command line syntax error.
# 3 - Specified file already exists.

import os
import sys
import argparse

import wolfy_util
import wolfy_config

argparser = argparse.ArgumentParser(prog='lw', description=
                                    'Create a new wolfy character. The COMBAT'
                                    ' SKILL and ENDURANCE options may be'
                                    ' utilized if the user prefers randomizing'
                                    ' his/her numbers using the original'
                                    ' Random Number Tables.')
argparser.add_argument('name', type = str, help =
                       'Desired character name. This'
                       ' will primarily act as the name of your character file'
                       ' which you may, in turn, version control.')
argparser.add_argument('-cs', '--combatskill', type = int, help =
                       'Your initial COMBAT SKILL. If this option is not'
                       ' specified, your initial COMBAT SKILL will be'
                       ' randomized for you.')
argparser.add_argument('-en', '--endurance', type = int, help =
                       'Your initial ENDURANCE. If this option is not given,'
                       ' your initial ENDURANCE will be automatically'
                       ' randomized.')
argparser.add_argument('-ac', '--active', action='store_true', help = 
                       'Whather or not to set the newly created character as'
                       ' active in the wolfy repository configuration.')
args = argparser.parse_args(sys.argv[1:])

name = args.name
combat_skill = args.combatskill
endurance = args.endurance
set_as_active = args.active

filename = name.lower() + '.lw'
if(os.path.isfile(filename)):
    argparser.error('There already exists a character with that name!'
                    ' Please remove ' + filename + ' or give a different'
                    ' character name.')
    sys.exit(3)
file = open(filename, 'w')

if combat_skill==None:
    combat_skill = str(wolfy_util.castD10() + 10)
    print('Character COMBAT SKILL not given.'
           'COMBAT SKILL is randomized to: ' + combat_skill)
if endurance==None:
    endurance = str(wolfy_util.castD10() + 20)
    print('Character ENDURANCE not given. ENDURANCE is randomized to: '
           + endurance)

file.write('# ' + filename + '\n'
           '# wolfy character file for Joe Dever\'s Lone Wolf series.\n'
           '# See https://github.com/CaterHatterPillar/wolfy\n'
           '# v. ' + wolfy_util.getVersionNumber() + '\n'
           '# Character: ' + name + '\n')
print('Created character ' + name + ' with filename ' + filename + '.')

if set_as_active:
    wolfy_config.setActiveChar(name)
    print('Set ' + name + ' as the active Lone Wolf character in the wolfy'
          ' repository configuration.')

file.close()
