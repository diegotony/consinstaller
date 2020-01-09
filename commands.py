import sys
import os
import click


def root():
    os.system("sudo".format(format))


def init_install():
    def check():
        update_packages()
        upgrade_packages()

    return check


def install_apt(package):
    os.system("sudo apt install {0} -y > /dev/null 2>&1".format(package))
    # print("Installing {0} ..".format(package))
    click.echo(click.style('Installing {0} ...'.format(
        package),
        # bg='black',
        fg='green',
        bold=True),
        err=True)


def update_packages():
    os.system("sudo apt update ")


def exit():
    os.system("exit")


def upgrade_packages():
    os.system("sudo apt upgrade")

