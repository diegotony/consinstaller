import sys
import os
import click
import yaml
import emoji

from commands import update_packages, install_packages
from utils import message_click_colors, init_cli

with open('yaml/packages.yml') as f:
    packages_docker = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/repos.yml') as f:
    repos_docker = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/url.yml') as f:
    url_docker = yaml.load(f, Loader=yaml.FullLoader)


def install_fast():
    init_cli()
    # message_click_colors(emoji.emojize(
    #     'Fast Install (Run Barry Run)'), "red", "yellow")
    update_packages()
    install_packages(
        packages_docker['packages_default'], "Default")
    install_packages(
        packages_docker['packages_admin'], "SysAdmin")
    install_packages(
        packages_docker['packages_utils'], "Utils")
