#!/bin/python
# lw.py
# Create a Lone Wolf character.

# Arguments:
# * Name: Character- and filename of instantiated character.
# * Combat Skill: Rolled COMBAT SKILL of character.
# * Endurance: Rolled ENDURANCE of character.
# (Don't specify Combat Skill or Endurance arguments if you wish them randomizd)

# System errors:
# 1 - Erronous arguments given.
# 2 - Command line syntax error.
# 3 - Specified file already exists.

import os
import sys
import getopt

import util

def print_help():
    print("Usage: " + sys.argv[0] + 
              " -n [--name] CHARACTER_NAME"
              " -cs [--combatskill] COMBAT_SKILL"
              " -en [--endurance] ENDURANCE")

# Entry point:
try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:cs:en:h', 
                                ['name=', 'combatskill=', 
                                 'endurance=', 'help='])
    if not opts:
        print("No arguments given!")
        print_help()
        sys.exit(1)
except getopt.GetoptError as e:
    print(e)
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print_help()
    elif opt in ('-n', '--name'):
        name = arg
    elif opt in ('-cs', '--combatskill'):
        combat_skill = arg
    elif opt in ('-en', '--endurance'):
        endurance = arg
    else:
        print_help()
        sys_exit(1)

try:
    name
except NameError:
    print("Argument -n [--name] NAME must be given!")
    print_help()
    sys_exit(1)
filename = name.lower() + ".lw"

if(os.path.isfile(filename)):
    print("There already exists a character with that name! Please remove " 
          + filename + " or give a different character name.")
    sys.exit(3)
file = open(filename, 'w')

try:
    combat_skill
except NameError:
    combat_skill = str(util.castD10() + 10)
    print("Character COMBAT SKILL not given."
           "COMBAT SKILL is randomized to: " + combat_skill)

try:
    endurance
except NameError:
    endurance = str(util.castD10() + 20)
    print("Character ENDURANCE not given. ENDURANCE is randomized to: "
           + endurance)

file.write("# " + filename + "\n"
           "# wolfy character file for Joe Dever's Lone Wolf series.\n"
           "# See https://github.com/CaterHatterPillar/wolfy\n#\n"
           "# Character: " + name + "\n")
print("Created character " + name + " with filename " + filename + ".")

file.close()
