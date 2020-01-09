import sys
import os


def root():
    os.system("sudo".format(format))


def init_install():
    def check():
        update_packages()
        upgrade_packages()

    return check


def install_apt(package):
    os.system("sudo apt install {0} > /dev/null".format(package))
    print("ok")


def update_packages():
    os.system("sudo apt update ")
    print("ok")


def exit():
    os.system("exit")


def upgrade_packages():
    os.system("sudo apt upgrade")
    print("ok")
