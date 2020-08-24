# import autofor modules
from environmentsetup import EnvironmentSetup
from title import header

# create main function


def main():

    # call header()
    header()

    # open main menu as a loop
    while True:
        EnvironmentSetup().mainmenu()


if __name__ == "__main__":
    main()
