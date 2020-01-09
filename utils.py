from pyfiglet import Figlet
from commands import init_install,install_apt
import os


quick_install = ['htop', 'glances']


def init_cli():
    f = Figlet(font='big')
    return f.renderText('Hello! Constantine1396')


def install_packages(packages_list):
    for package in packages_list:
        install_apt(package)
        print(package)
