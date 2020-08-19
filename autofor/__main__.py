# import autofor modules
from autofor.environmentsetup import EnvironmentSetup
from autofor.tools import Tools
from autofor.title import header

# create main function


def main():

    # call header()
    header()

    # open main menu as a loop
    while True:
        EnvironmentSetup().mainmenu()


if __name__ == "__main__":
    main()
