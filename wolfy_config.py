import os
import sys
import ConfigParser

Config_File = '.wolfy'

class Config:
    def __init__(self, active_char):
        self.active_char = active_char

def parseConfig():
    config_file = open(Config_File, 'r')
    config_parser = ConfigParser.RawConfigParser()
    config_parser.read(Config_File)
    
    config = Config(config_parser.get('wolfy', 'ACTIVE_CHAR'))

    if(config.active_char=='NA'):
        print('ACTIVE_CHAR is NA! Please set an active character before'
              ' continuing.')
        sys.exit(2)
    return config

def getConfig():
    if not os.path.isfile(Config_File):
        print('wolfy repository not initialized!'
              ' Please initialize wolfy using the init-command!')
        sys.exit(1)
    return parseConfig()
