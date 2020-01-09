from pyfiglet import Figlet,figlet_format
from commands import init_install, install_apt
import os
import click

def init_cli():
    f = Figlet(font='big')
    return f.renderText('Hello! Constantine1396')

def packages_gui(name):
    result = figlet_format("Packages {0}".format(name), font = "digital" ) 
    return result


def install_packages(packages_list, name):
    size = int(len(packages_list))*100
    print(packages_gui(name))
    for package in packages_list:
        install_apt(package)
