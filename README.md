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

autofor has been designed to meet aims and objectives of a master's project. In
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

To install these packages you can copy and paste the following...

```
sudo apt update
sudo apt-get install -y exiftool foremost

```

Setup
------------------
As autofor is written in python3, which is an interpretive language, it can't easily be
compiled and installed in the same fashion as some other programs. As such, in it's alpha
form, autofor can be installed as a python package. Although not the same as installing some
other binary file, it can be run in a similar fashion from the terminal.

- **Downloading from Github**

	- autofor has been uploaded to my GitHub for version control and distribution. To download it from
	GitHub follow these steps:

- **Check you have 'git' installed on your system**
	- For Debian based Linux distributions, git can be installed by runnning:

	```
	sudo apt install git
	```

- **Download with git**
	- Once git has been installed navigate (using `cd`) to a directory where you would like to download autofor.
	- Once there, run the following to download (clone) the autofor source files:

	```
	git clone https://github.com/timbees44/autofor
	```

- **Installation**
	- Navigate to into the autofor directory (`cd autofor`) that has been downloaded.
	- Using `ls` you should see a "setup.py" file in the directory amongst other folders and files.
	- To install do the following:

	```
	sudo python3 setup.py install
	```

	- Providing the installation has worked, autofor should now be usable from any directory in the terminal

Usage
----------------
**Launching autofor**
- To launch autofor, you can simply type `autofor` into the terminal and hit Enter

**Working with autofor**
- 




