autofor
==============

> Tim Burrey | 24th September, 2020

-----------------

**Documentation:** 

This tool aims to help in the automation of basic digital forensic tasks. It is
also aimed at being usable and learnable for those with limited IT or digital
forensic backgrounds.

AutoFor is written in Python 3.



DISCLAIMER
----------

Autofor has been designed to meet aims and objectives of a master's project. In
it's current state it should **NOT** be treated as a replacement for tried and tested
digital forensics software.

Part of this tool's function is to extract information from various files and file
systems. As such it should only be used on systems that you own or have been given
permission to use. It should also only be used against files and file systems that
you own or have permission to access.

Getting Started
---------------

At this stage of development, autofor has been designed to solely work on Linux. 
Most testing has been done on a ubuntu 20.04 system.

I recommend running this with the latest version of Python.

**On Ubuntu**

Two Linxu tools will be needed in order for the full function of autofor.

These are:
- exiftool

	Exiftool is used to extract metadata from files. This can be used for file
	type identification and provide time information regarding the interactions
	with files

- foremost

	Foremost is used to recover files. In autofor, it has initially been used to search
	for embedded or composite files. This can occur when a user concatenates two files.

Autofor will automatically check if these tools are installed. If they aren't it will try
to install them. If autofor fails to do so, they can be installed manually as shown below

To install these packages you can copy and paste the following...

```
sudo apt update
sudo apt-get install -y exiftool foremost

```

Setup
------------------
As autofor is written in python3, which is an interpretive language, it can't easily be
compiled and installed in the same fashion as some other programs. As such, in it's alpha
form, autofor can only be run from the directory it is downloaded to. Packaging the and creating
a working setup.py is something that will be worked on for future iterations of the project.

- **Downloading from Github**

	- autofor has been uploaded to my GitHub for version control and distribution. To download it from
	GitHub follow these steps:

- **Check you have 'git' installed on your system**
	- For Debian based Linux distributions, git can be installed by running:

	```
	sudo apt install git
	```

- **Download with git**
	- Once git has been installed navigate (using `cd`) to a directory where you would like to download autofor.
	- Once there, run the following to download (clone) the autofor source files:

	```
	git clone https://github.com/timbees44/autofor
	```

Usage
----------------
**Launching autofor**
- To launch autofor, you can simply type `python3 autofor.py` into the terminal and hit Enter
- As stated above you must be in the directory with the autofor.py file for it to run.

**Working with autofor**
- There may be issues with usability as autofor is still in a prototype stage of development.
- Note that to view a lot of information that autofor extracts you will need to go to the 
securestore directory that you will make in the early phase of an investigation. From here you 
will be able to see extracted information in the "analysis" directory, carved files in the "tests"
directory, the original file in the "image" directory and an extracted/copied file in the "logical"
directory which will be used for running the tests.
- For disk images (.dd, .raw) these will have been mounted in "/mnt/...."




