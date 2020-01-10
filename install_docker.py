import sys
import os
import click
import yaml
from commands import update_packages, install_packages
from utils import message_click_colors, message_click


with open('yaml/packages.yml') as f:
    packages_docker = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/repos.yml') as f:
    repos_docker = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/url.yml') as f:
    url_docker = yaml.load(f, Loader=yaml.FullLoader)


def install_docker():
    message_click(
        "(¯`·._.··¸.-~*´¨¯¨`*·~-.,-(_Docker Instalation_)-,.-~*´¨¯¨`*·~-.¸··._.·´¯)\n", "cyan")
    update_packages()
    install_packages(
        packages_docker['packages_pre_docker'], "Docker Pre-Instalation")
    message_click("Added Docker’s official GPG key", "cyan")
    docker_curl(url_docker['docker']['url'])
    message_click("Verify fingerprint", "cyan")
    docker_apt_key()
    message_click("Adding Repository ...", "cyan")
    docker_repo(repos_docker['docker']['arch'], repos_docker['docker']['url'])
    update_packages()
    install_packages(
        packages_docker['packages_post_docker'], "Docker Post-Instalation")
    message_click("Testing Docker", "cyan")
    check_docker()
    message_click("Create docker group", "cyan")
    create_group_docker()
    add_group_docker()


def docker_curl(url):
    os.system(" curl -fsSL {0} | sudo apt-key add -".format(url))


def docker_apt_key():
    os.system("sudo apt-key fingerprint 0EBFCD88")


def docker_repo(arch, url):
    os.system("sudo add-apt-repository \
   'deb [arch={0}] {1} \
   buster \
   stable'".format(arch, url))


def check_docker():
    os.system("sudo docker run hello-world")


def create_group_docker():
    os.system("sudo groupadd docker")


def add_group_docker():
    os.system("sudo usermod -aG docker $USER")
