# modules to check if required dependencies installed
import importlib.util
import sys

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

# iterate through dependencies list
for package in dependencies:
    # check if the package is installed
    if package in sys.modules:
        pass
    # if not, find the package
    elif (spec := importlib.util.find_spec(package)) is not None:
        # set the package to be installed
        module = importlib.util.module_from_spec(spec)
        sys.modules[package] = module
        # install the package
        spec.loader.exec_module(module)
        print(f"{package} has been imported")
    # give warning if package wasn't installed
    else:
        print(f"{package} not found. Autofor may fail to run")


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
