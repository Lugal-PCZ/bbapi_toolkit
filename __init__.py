import os
import sys
import configparser


modulepath = os.path.dirname(__file__)
configfile = 'config.ini'
if not os.path.exists('{}/{}'.format(modulepath, configfile)):
    print()
    sys.tracebacklimit = 0
    raise FileNotFoundError('\nThe config.ini file is missing.\nPlease copy the config.ini.example file to config.ini and fill out the appropriate ON API and/or SKY API settings for this project.\n')
else:
    CONFIG = configparser.RawConfigParser()
    CONFIG.read('{}/{}'.format(modulepath, configfile))
