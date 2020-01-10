import sys
import os
import click
from utils import packages_gui, message_gui, message_click_colors, message_click


def root():
    os.system("sudo".format(format))


def init_install():
    def check():
        update_packages()
        upgrade_packages()

    return check


def install_apt(package):
    cmd = os.system("sudo apt install {0} -y > /dev/null 2>&1".format(package))
    message_click(('Installing {0} ...'.format(package)), "yellow")
    if cmd == 0:
        message_click(
            (' {0} installed    \,,/(^_^)\,,/ '.format(package)), "green")

    else:
        message_click((' {0} not installed    <*_*>  '.format(package)), "red")

        pass
    # print("Installing {0} ..".format(package))


def update_packages():
    print(message_click(
        '           (¯`·._.·(¯`·._.· Updating Packages  ·._.·´¯)·._.·´¯)\n', "green"))
    os.system("sudo apt-get update > /dev/null ")


def exit():
    os.system("exit")


def upgrade_packages():
    os.system("sudo apt-get upgrade -y > /dev/null 2>&1")


def install_packages(packages_list, name):
    size = int(len(packages_list))*100
    print(message_click(
        '\n     (¯`·._.·(¯`·._.·   Installing {0} Packages   ·._.·´¯)·._.·´¯)\n'.format(name), "magenta"))

    for package in packages_list:
        install_apt(package)
