# modules to check if required dependencies installed
import sys
import subprocess
import pkg_resources

# import autofor modules
from environmentsetup import EnvironmentSetup
from title import header


"""
As this version of autofor will be used as a portable tool (won't be installed
on users system), it is necessary to check that the required dependencies have
been installed for the program to run. Usually the this would be handled in the
"setup.py" script during installation. In this case it is being handled prior
to the launch of the tool. Due to the small number of dependencies required it
should not take too long to check before the tool successfully launches.
"""
# check for dependencies
# adapted from https://stackoverflow.com/questions/1051254/check-if-python-package-is-installed
dependencies = [
    "filetype",
    "openpyxl",
    "simple_term_menu",
    "pandas"
]

required = {"filetype",
            "openpyxl",
            "simple_term_menu",
            "pandas"
            }
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


# create main function
def main():

    # call header()
    header()

    # open main menu as a loop
    while True:
        EnvironmentSetup().mainmenu()


# call main
if __name__ == "__main__":
    main()
