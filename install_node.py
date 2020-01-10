import sys
import os
import click
import yaml
import emoji

from commands import update_packages, install_packages, install_apt
from utils import message_click_colors, message_click

with open('yaml/packages.yml') as f:
    packages = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/url.yml') as f:
    url = yaml.load(f, Loader=yaml.FullLoader)


def install_node(version):
    message_click(
        "\n(¯`·._.··¸.-~*´¨¯¨`*·~-.,-(_NodeJs Instalation_)-,.-~*´¨¯¨`*·~-.¸··._.·´¯)\n", "cyan")
    update_packages()
    message_click("Adding Repository ... ", "green")
    node_curl(url['nodejs']['url'], version)
    install_apt(packages['packages_pre_node'])


def node_curl(url, version):
    os.system(
        "curl -sL {0}{1}.x | sudo -E bash -  > /dev/null".format(url, version))
