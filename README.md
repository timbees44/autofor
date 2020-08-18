AutoFor
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

At this stage of development, Autofor has been designed to solely work on Linux. 
Most testing has been done on a ubuntu 20.04 system.

I recommend running this with the latest version of Python.

**On Ubuntu**

Two Linxu tools will be needed in order for the full function of Autofor.

These are:
- exiftool

	Exiftool is used to extract metadata from files. This can be used for file
	type identification and provide time information regarding the interactions
	with files

- foremost

	Foremost is used to recover files. In Autofor, it has initially been used to search
	for embedded or composite files. This can occur when a user concatenates two files.

To install these packages you can copy and paste the following...

```
sudo apt update
sudo apt-get install -y exiftool foremost

```

**Setup**

ADD THIS!

Usage
----------------




Framework Methodology
---------------------


