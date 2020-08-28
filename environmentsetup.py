# python libraries
import os
import sys
import subprocess
import shutil
import zipfile
import tarfile
import hashlib
import json
import csv
import time
# dependencies
import filetype
import openpyxl
from tkinter import *
from tkinter import filedialog
from simple_term_menu import TerminalMenu
# autofor python modules
from tools import Tools
from title import header


# class for Forensic Environment. This stores variables for the forensic environment that might need to be called at later stages of the program


class EnvironmentSetup:
    # class variables that may be used both in and out of class
    case_name = ""
    secure_store_location = ""
    evidence = ""
    mount_point = ""

    def __init__(self):
        pass

    # start menu
    def startmenu(self):
        start_menu_title = "Please select an option to get started."
        start_menu_items = ["New Investigation",
                            "Continue Investigation"]
        start_menu_exit = False

        start_menu = TerminalMenu(title=start_menu_title,
                                  menu_entries=start_menu_items)

        while not start_menu_exit:
            item_sel = start_menu.show()

            # Item "0" is option to start new investigation
            if item_sel == 0:
                self.casename()
                self.choosesecurestore(self.case_name)
                self.fileselection()
                self.secstorebuild()
                self.spreadsheet(self.secure_store_location, self.case_name)
                self.evidencetype(self.evidence, self.secure_store_location)
                Tools().files(self.secure_store_location,
                              self.mount_point, self.case_name)
                Tools().carver(self.secure_store_location, self.mount_point, self.case_name)
                Tools().dir_tree(self.mount_point, self.secure_store_location)
                Tools().regexsearch(self.secure_store_location, self.mount_point, self.case_name)

                start_menu_exit = True

            # item "1" is option to continue with a case.
            # this will ask user to select secure store location where config file will be found and user can pick up from where they left off.
            elif item_sel == 1:
                # user will need to enter case name/number
                # this will be used as arg for config read method
                self.configread()
                # take another hash depending on whether evidence is disk image or in logical
                if self.mount_point == "":
                    path = self.secure_store_location + "/logical"
                    if not os.path.isdir(path):
                        print(
                            "It looks like your secure store hasn't been setup or is missing.")
                        print(
                            "You may wish to restart case/rebuild securestore or check secure store path and make sure there is a valid secure store there")
                else:
                    path = self.mount_point
                    if not os.path.isdir(path):
                        print("It looks like your evidence is no longer mounted.")
                        print("Trying to remount...")
                        self.evidencetype(self.evidencetype,
                                          self.secure_store_location)
                        if not os.path.isdir(path):
                            print(
                                "There seems to be issues with mounting your evidence image.")
                            print("You may wish to restart your case")
                        else:
                            print("Evidence mounted correctly")
                            print("You can proceed with investigation!")

                Tools().hash(self.case_name, path, self.secure_store_location)

                print(
                    f"Taken another hash of {path} to ensure chain of analysis upheld")

                start_menu_exit = True
            break

    # main menu for case continuation and other tools
    def mainmenu(self):
        main_menu_title = "Please select from the following options!"
        main_menu_items = ["Start/Continue Investigation", "Examine evidence analysis",
                           "Word/Term Search", "Take hash(es)", "Exit"]
        main_menu_exit = False

        main_menu = TerminalMenu(title=main_menu_title,
                                 menu_entries=main_menu_items)

        while not main_menu_exit:
            item_sel = main_menu.show()

            # item 0 will take user to startmenu
            if item_sel == 0:
                self.startmenu()

            # show evidence analysis file(s) for user to open and examine
            elif item_sel == 1:
                # get case
                print("Sorry, this feature is not available yet")
                print(
                    "Analysis documents of evidence can be found in the 'analysis' directory of the securestore path for each case.")
                time.sleep(5)
                self.mainmenu()

            # item 2 will allow users to search for a partiular word or phrase in all files or a specific file/directory
            elif item_sel == 2:
                Tools().wordsearch(self.secure_store_location, self.mount_point)
                mm = input("Press \033[94mENTER\033[0m to return to main menu")
                if mm == "":
                    os.system("clear")
                    self.mainmenu()

            # item 3 will allow users to take a hash of work dir (either logical or mount point) or a specific file/directory
            elif item_sel == 3:
                # get user to input path to hash
                hash_menu_title = "Choose File or Directory to hash"
                hash_menu_items = ["File", "Directory", "Back"]
                hash_menu_exit = False

                hash_menu = TerminalMenu(title=hash_menu_title,
                                         menu_entries=hash_menu_items)

                while not hash_menu_exit:
                    item_sel = hash_menu.show()

                    # check file
                    if item_sel == 0:
                        path = input(
                            "Enter file path here or press \033[94mENTER\033[0m to use graphic user interface")
                        if path == "":
                            root = Tk()
                            root.withdraw()
                            path = root.file = filedialog.askopenfilename()

                        Tools().hash(self.case_name, path,
                                     self.secure_store_location)

                    # check dir
                    elif item_sel == 1:
                        path = input(
                            "Enter directory path here or press \033[94mENTER\033[0m to use graphic user interface")
                        if path == "":
                            root = Tk()
                            root.withdraw()
                            path = root.directory = filedialog.askdirectory()

                        Tools().hash(self.case_name, path,
                                     self.secure_store_location)

                    # back to main menu
                    elif item_sel == 2:
                        pass

                    hash_menu_exit = True

            # exit program
            elif item_sel == 4:
                os.system("clear")
                print("Note! There may still be some mounted drives in '/mnt/...'")
                sys.exit()

    # user enters case name
    def casename(self):
        cname = input("Please type a case name/number: ")
        self.case_name = cname
        self.configmake(self.case_name)
        self.configupdate()

    # user chooses securestore path
    def choosesecurestore(self, case):
        # explain why securestore
        print("\nTo use many of the automated features that this forensic tool provides, you must set up a secure store directory\nIf you already have one, you can select it with the GUI or by entering the path.")
        while True:
            # user has option to input by typing path or using gui
            path = input(
                "Use the graphic user interface to choose secure store location - press \033[94mENTER\033[0m.\n\u001b[31mOR\u001b[0m enter path to secure store here: ")
            # if user presses enter when prompted it will result in empty string and go to gui condition
            if path == "":
                root = Tk()
                root.withdraw()
                path = root.directory = filedialog.askdirectory()
            # else path user has entered will be chosen - *NEED TO ALLOW FOR USER ERRORS AND HANDLE ACCORDINGLY*
            elif os.path.isdir(path):
                pass

            else:
                print(
                    "The path you have chosen doesn't seem to be valid, please check and try again\n")

            break

        # check if path they have chosen looks like a secure store
        # assign path variable to the class "secure_store_location" variable so it can be used globally
        if ('image' and 'logical' and 'analysis' and 'notes' and 'history' and 'staff' and 'tests' and 'reports') in os.listdir(path):
            self.secure_store_location = path
        else:
            self.secure_store_location = f"{path}/securestore_{case}"

        self.configupdate()

    # method to select file or directory to be used, using simple term menu
    def fileselection(self):
        main_menu_title = "What would you like to investigate?"
        main_menu_items = ["Directory/Folder", "File"]
        main_menu_exit = False

        main_menu = TerminalMenu(title=main_menu_title,
                                 menu_entries=main_menu_items)

        while not main_menu_exit:
            item_sel = main_menu.show()

            # Item "0" is option to select a directory to work with
            if item_sel == 0:
                while True:
                    # user has option to input by typing path or using gui
                    path = input(
                        "Use the graphic user interface to choose Directory - press \033[94mENTER\033[0m.\n\u001b[31mOR\u001b[0m enter path to directory here: ")
                    # if user presses enter when prompted it will result in empty string and go to gui condition
                    if path == "":
                        root = Tk()
                        root.withdraw()
                        path = root.directory = filedialog.askdirectory()

                    elif os.path.isdir(path):
                        pass

                    else:
                        print(
                            "The path you have chosen doesn't seem to be valid, please check and try again\n")

                    break
                main_menu_exit = True

            # item "1" is to select a file to work with. This can be any file type and will be processed accordingly.
            elif item_sel == 1:
                while True:
                    # user has option to input by typing path or using gui
                    path = input(
                        "Use the graphic user interface to choose FILE location - press \033[94mENTER\033[0m.\n\u001b[31mOR\u001b[0m enter path to FILE here: ")
                    # if user presses enter when prompted it will result in empty string and go to gui condition
                    if path == "":
                        root = Tk()
                        root.withdraw()
                        path = root.file = filedialog.askopenfilename()
                    # else path user has entered will be chosen - *NEED TO ALLOW FOR USER ERRORS AND HANDLE ACCORDINGLY*
                    elif os.path.isfile(path):
                        pass

                    else:
                        print(
                            "The path you have chosen doesn't seem to be valid, please check and try again\n")
                    break
                main_menu_exit = True

            # define class wide varaible from method
            self.evidence = path

            self.configupdate()

    # this method lays out the terminal menu for users to build their securestore
    def secstorebuild(self):
        sspath = self.secure_store_location
        # print(sspath)
        while True:
            if os.path.isdir(sspath) and ('image' and 'logical' and 'analysis' and 'notes' and 'history' and 'staff' and 'tests' and 'reports') in os.listdir(sspath):
                gotsc_menu_title = f"It looks like {sspath} is already a secure store.\nWould you like to use it?"
                gotsc_menu_items = ["Yes", "No",
                                    "Rename case"]
                gotsc_menu_exit = False
                gotsc_menu = TerminalMenu(
                    title=gotsc_menu_title, menu_entries=gotsc_menu_items)
                while not gotsc_menu_exit:
                    item_sel = gotsc_menu.show()
                    if item_sel == 0:
                        gotsc_menu_exit = True
                        break
                    elif item_sel == 1:
                        self.choosesecurestore(self.case_name)
                        gotsc_menu_exit = True
                    elif item_sel == 2:
                        self.casename()
                        print(f"case renamed to {self.case_name}")
                        # call to mainmenu... *Need to build one!*
                        gotsc_menu_exit = True

            else:
                os.mkdir(sspath)
                folders = ['image', 'logical', 'analysis', 'notes',
                           'history', 'staff', 'tests', 'reports']
                for folder in folders:
                    os.mkdir(os.path.join(sspath, folder))

                print(
                    f"\033[1; 32; 40mSecure Store made successfully\033[0m at {sspath}")

            break

    # taking spreadsheet template from config files included with programme and saving into secure store with case name
    def spreadsheet(self, sspath, case):
        excelsheet = os.path.dirname(os.path.abspath("excel_temp.xlsx"))
        wb = openpyxl.load_workbook(
            excelsheet + "/config_files/excel_temp.xlsx")
        wb.save(f'{sspath}/analysis/spreadsheet_{case}.xlsx')

    # making a config file to allow for persistance with cases. template
    def configmake(self, cname=case_name):
        config = {"CaseID": "",
                  "SSPath": "",
                  "EvidenceFile": "",
                  "MountPoint": ""}

        config_path = os.path.dirname(os.path.abspath(
            "case_logs/*")) + f"/{cname}.json"

        with open(config_path, "w") as f:
            json.dump(config, f)

    # allows for config file update with key variables
    def configupdate(self):
        config_path = os.path.dirname(os.path.abspath(
            "case_logs/*")) + f"/{self.case_name}.json"
        # print(config_path)

        with open(config_path, 'r') as f:
            config = json.load(f)

        config["CaseID"] = self.case_name
        config["SSPath"] = self.secure_store_location
        config["EvidenceFile"] = self.evidence
        config["MountPoint"] = self.mount_point

        with open(config_path, 'w') as f:
            json.dump(config, f)

    # returns values from config file to dictionary so they can be used to set Input variables
    # used when continuing with an investigation
    def configread(self):
        # get user to input case number
        file = input("Please enter case name/number here: ")
        # use * to get list of case_logs path
        dir = os.listdir(os.path.dirname(os.path.abspath(
            "case_logs/*")))

        # check if the json file is case_logs dir
        for i in dir:
            # or condition in case user enters case name with .json
            if file == i[:-5] or file == i:
                print("File Found!")
                path = str(os.path.dirname(os.path.abspath(
                    "case_logs/*"))) + "/" + str(i)

                with open(path, 'r') as f:
                    config = json.load(f)

                    self.case_name = config["CaseID"]
                    self.secure_store_location = config["SSPath"]
                    self.evidence = config["EvidenceFile"]
                    self.mount_point = config["MountPoint"]

                    f.close()

                print("Case parameters retrieved from log file!")
                print("So long as the location of your securestore and evidence haven't changed you can continue with examination and analysis")
                Tools().hash(self.case_name, self.evidence, self.secure_store_location)

            # options for if file not found
            else:
                while True:
                    print(
                        "There doesn't seem to be a case log file that matches your input")
                    print(
                        "Please try again! Alternatively Press \033[94mENTER\033[0m to view a list of case names")
                    user_input = input(
                        "\033[31mOR\u001b[0m type \033[92mback\033[0m and press \033[94mENTER\033[0m to go back to start: ")
                    if user_input == "":
                        case_list = os.listdir(os.path.dirname(os.path.abspath(
                            "case_logs/*")))
                        print(case_list)
                        continue
                    elif user_input == "back" or "back".upper() or "b" or "Back":
                        pass
                    else:
                        pass

                    break
                self.configread()

    # evidencetype method used to handle file or directory accordingly
    def evidencetype(self, evidence, sspath):
        # take initial hash of file/dir
        Tools().inithash(
            self.case_name, self.secure_store_location, self.evidence)
        # split filename from path set as method variable
        filename = evidence.split("/")[-1]
        # check if file or dir
        if os.path.isfile(evidence):
            # copy file to securestore
            os.system(f"sudo cp {evidence} {sspath}/image")
            print("copying to image folder in securestore...")
            # check file type of evidence
            if not tarfile.is_tarfile(evidence) or not zipfile.is_zipfile(evidence):
                # copy to logical to work with file
                imagefile = f"{sspath}/image/{filename}"
                os.system(
                    f"sudo cp {sspath}/image/{filename} {sspath}/logical")
                logfile = f"{sspath}/logical/{filename}"
                # carve out file type from linux "file" query
                file_out = subprocess.check_output(
                    ["file", logfile]).decode("utf-8")
                ftype = file_out.split(":")[1].split(",")[0].split()[0].upper()
                # open file_type csv in config_files to find filetype
                file = open(os.path.dirname(
                    os.path.abspath("file_type.csv")) + "/config_files/file_type.csv", "r")
                for line in file:
                    ft = line.split(",")[0]
                    filedescription = line.split(",")[1]
                    if ft.upper() == ftype.upper():
                        print("Looks like you're working with a " +
                              filename + ": " + filedescription)
                        break
                    elif (ft.upper() in ftype.upper()) and not (ft.upper() == ftype.upper()):
                        print("Possible match to filetype is: " +
                              filename + ": " + filedescription)
                        break
                    elif filetype.guess(logfile) is not None:
                        print('File extension: %s' %
                              filetype.guess(logfile).extension)
                        print('File MIME type: %s' %
                              filetype.guess(logfile).mime)
                        break
                    else:
                        print(
                            "This file type is unknown, autofor will still try to examine it")
                        break
                # hash for files
                Tools().hash(self.case_name,
                             f"{sspath}/logical/{filename}", self.secure_store_location)

            # check if disk image file
            if "DOS/MBR" in ftype:
                print(
                    f"Looks like {filename} is a disk image, Autofor will mount it for you...")
                fsplit = file_out.split(" ")
                if "startsector" in fsplit:
                    offset = int(
                        fsplit[(fsplit.index("startsector") + 1)][:-1]) * 512
                    # exceptions for creating directory if exists. Don't seem to work**
                else:
                    offset = 0
                # create mount location with max 10 characters for so not too messy
                fname = logfile.split("/")[-1][:10]
                try:
                    print("Making mount directory...")
                    os.system(f"sudo mkdir /mnt/{fname}")
                except FileExistsError:
                    print(
                        "Looks like this mount point already exists... Mounting...")
                # mount disk image. Haven't used exceptions
                os.system(
                    f"sudo mount -o ro,loop,offset={offset} {logfile} /mnt/{fname}")
                self.mount_point = f"/mnt/{fname}"
                # update config json
                self.configupdate()
                # success
                print("Mount Complete!")
                # hash all files in mount point
                Tools().hash(self.case_name,
                             self.mount_point, self.secure_store_location)

            # handling compressed images
            elif tarfile.is_tarfile(imagefile):
                print(f"Looks like {filename} is a tarfile")
                print(f"extracting to {sspath}/logical")
                # print(imagefile)
                f = tarfile.open(imagefile)
                f.extractall(path=f'{sspath}/logical')
                f.close()
                print("Extraction complete")

                Tools().hash(self.case_name,
                             f"{sspath}/logical/{filename}", self.secure_store_location)

            elif zipfile.is_zipfile(imagefile):
                print(f"Looks like {filename} is a zipfile")
                print(f"extracting to {sspath}/logical")
                f = zipfile.ZipFile(imagefile)
                f.extractall(path=f'{sspath}/logical')
                print("Extraction complete")
                f.close()

                Tools().hash(self.case_name,
                             f"{sspath}/logical", self.secure_store_location)

        elif os.path.isdir(evidence):
            # zip directory to image folder in securestore
            print(f"{filename} is a directory")
            print(f"{filename} will be compressed to {sspath}/image")
            print(
                f"{filename} will then be extracted to {sspath}/logical/{filename} for analysis")
            """shutil makes archiving dirs easier. No issues with path confusion that
            can be experienced with using zipfile and having to iterate through
            all of the files and subdirs in the root dir"""
            shutil.make_archive(
                f"{sspath}/image/{filename}", 'zip', evidence)
            # extract from image to logical
            with zipfile.ZipFile(f'{sspath}/image/{filename.split("/")[-1]}.zip', 'r') as zip:
                # make directory in logical incase archives are in root of archive
                os.system(f"mkdir {sspath}/logical/{filename}")
                zip.extractall(f"{sspath}/logical/{filename}")

            # Take second hash of logical output for dir
            Tools().hash(self.case_name,
                         f"{sspath}/logical/{filename}", self.secure_store_location)
