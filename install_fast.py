import sys
import os
import click
import yaml
import emoji

from commands import update_packages, install_packages_apt
from utils import message_click_colors, init_cli

with open('yaml/packages.yml') as f:
    packages = yaml.load(f, Loader=yaml.FullLoader)


def install_all():
    update_packages()
    install_packages_apt(
        packages['packages_default'], "Default")


