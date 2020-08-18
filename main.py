# import os and subprocess to interact with operating system
import subprocess
import os
# import platform to check what os is being used
import platform
# import title.py for heading artwork and intro
import title
# import EnvironmentSetup
from EnvironmentSetup import *


# display programme title logo
title.header()

# project name function

# start menu to find file type and make securestore etc
x = EnvironmentSetup()
x.startmenu()
print(x.case_name)
print(x.secure_store_location)
print(x.evidence)
x.secstorebuild()
x.spreadsheet(x.secure_store_location, x.case_name)
