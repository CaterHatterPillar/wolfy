#!/bin/python
# kd.py
# Add a Kai Discipline to a Lone Wolf character.

import os
import sys
import operator
import argparse

import wolfy_char
import wolfy_config

# These may change as the player progresses throughout the books, but
# should do for the first five:
Kai_Disciplines = ['camouflage', 'hunting', 'sixth sense', 'tracking',
                   'healing', 'weaponskill', 'mindshield', 'mindblast',
                   'animal kinship', 'mind over matter']
Weapon_Skills = {'dagger':0,
                 'spear':1,
                 'mace':2,
                 'short sword':3,
                 'warhammer':4,
                 'axe':6,
                 'sword':[5, 7],
                 'quarterstaff':8,
                 'broadsword':9}

argparser = argparse.ArgumentParser(prog='kd', description=
                                    'Add a Kai Discipline to a wolfy'
                                    ' character.')
argparser.add_argument('skill', type = str, choices = Kai_Disciplines,
                       help = 'The Kai Discipline to add to active character.')
argparser.add_argument('-t', '--type', type = int,
                       help = 'Additional Skill type option required by some'
                       ' Disciplines (Weaponskill).')
args = argparser.parse_args(sys.argv[1:])

skill = args.skill
type = args.type
if skill=='weaponskill' and type==None:
    argparser.error('Additional Type option must be given for'
                    ' Kai Discipline Weaponskill! Please specify weapon'
                    ' proficiency [0-9]:\n'
                    + str(sorted(Weapon_Skills.iteritems(),
                                 key = operator.itemgetter(1))))

config = wolfy_config.getConfig()
char = wolfy_char.getChar(config.active_char)
