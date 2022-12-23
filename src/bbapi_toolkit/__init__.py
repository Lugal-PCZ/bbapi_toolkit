import os.path
import shutil

if not os.path.exists("config.ini.example"):
    packagepath = os.path.dirname(__file__)
    shutil.copy(packagepath + "/config.ini.example", "config.ini.example")
