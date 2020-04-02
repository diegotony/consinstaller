import sys
import os
import click
import yaml

from commands import update_packages, install_packages_apt, install_apt
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


def install_node_all(version):
    message_click(
        "\n(¯`·._.··¸.-~*´¨¯¨`*·~-.,-(_NodeJs Instalation_)-,.-~*´¨¯¨`*·~-.¸··._.·´¯)\n", "cyan")
    update_packages()
    message_click("Adding Repository ... ", "green")
    node_curl(url['nodejs']['url'], version)
    install_apt(packages['packages_pre_node'])
    install_packages_npm(packages['packages_npm'])


def node_curl(url, version):
    os.system(
        "curl -sL {0}{1}.x | sudo -E bash -  > /dev/null".format(url, version))


def install_npm(package):
    cmd = os.system("sudo npm i -g  {0} -y > /dev/null 2>&1".format(package))
    message_click(('Installing {0} ...'.format(package)), "yellow")
    if cmd == 0:
        message_click(
            (' {0} installed    \,,/(^_^)\,,/ '.format(package)), "green")

    else:
        message_click((' {0} not installed    <*_*>  '.format(package)), "red")


def install_packages_npm(packages_list):
    print(message_click(
        '\n     (¯`·._.·(¯`·._.·   Installing Node Packages   ·._.·´¯)·._.·´¯)\n', "magenta"))
    for package in packages_list:
        install_npm(package)
