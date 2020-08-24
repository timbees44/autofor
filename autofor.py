# modules to check if required dependencies installed
import sys
import subprocess
import os


"""
As this version of autofor will be used as a portable tool (won't be installed
on users system), it is necessary to check that the required dependencies have
been installed for the program to run. Usually the this would be handled in the
"setup.py" script during installation. In this case it is being handled prior
to the launch of the tool. Due to the small number of dependencies required it
should not take too long to check before the tool successfully launches.
"""
# check for dependencies
dependencies = [
    "filetype",
    "openpyxl",
    "simple-term-menu",
    "pandas"
]

# empty list to append any missing dependencies to
missing_deps = []

# check pip3 list of installed python modules
installed_mods = subprocess.check_output(
    "pip3 list", stderr=subprocess.STDOUT, shell=True).decode("utf-8")
# iterate through our dependency list to check if any are missing
for i in dependencies:
    # append to 'missing_deps' list if not in pip3 list
    if i not in installed_mods:
        missing_deps.append(i)

# check if user is actually missing modules
if missing_deps == []:
    pass
else:
    # let user know that they need to install certain modules for the tool to run
    print("You are missing the following modules that autofor needs to run, would you like to install?")
    print(missing_deps)
    # allow for user choice
    user_input = input(
        "Press \033[94mENTER\033[0m to install or type 'q' to exit")
    if user_input == "":
        print(f"Installing {missing_deps}")
        # using os. Subprocess likely preferred but not as straight forward/robust as os
        os.system(f"pip3 install {', '.join(missing_deps)}")

    elif user_input == "q" or "quit":
        # exit program if user
        sys.exit()


# create main function
def main():

    # import autofor modules
    from environmentsetup import EnvironmentSetup
    from title import header

    # call header()
    header()

    # open main menu as a loop
    while True:
        EnvironmentSetup().mainmenu()


# call main
if __name__ == "__main__":
    main()
