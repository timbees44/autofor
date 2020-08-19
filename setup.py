"""
This is the setup file for autofor. Along with the README.md file,
this will highlight key information about the project regarding
dependencies and version information.

It's main role is to install the autofor project and it's accompanying
files onto a local system for ease of access and use.
"""
# setuptools library used for setting up all facets of python package
from setuptools import setup, find_packages

# list of dependencies needed to be installed by pip3.
# Other libraries and modules are native to python
dependencies = [
    "filetype",
    "openpyxl",
    "simple_term_menu",
    "pandas"
]

# Setup
setup(
    name="autofor",
    version="1.0",
    description="Automated Digital Forensic Tool Suite",
    author="Tim Burry",
    author_email="s5224241@bournemouth.ac.uk",
    url="https://github.com/timbees44/autofor",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Digital Forensic Students and Professionals",
        "Topic :: Digital Forensics :: Automation :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    packages=find_packages(),
    package_data={
        "excel_temp.xlsx": ["config_files/excel_temp.xlsx"],
        "file_sigs.csv": ["config_files/file_sigs.csv"]
        "case_logs": ["case_logs/*"]
    },
    entry_points={"console_scripts": ["autofor=autofor.__main__:main"]},
    install_requires=dependencies,
)
