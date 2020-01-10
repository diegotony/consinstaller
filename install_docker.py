import sys
import os
import click
import yaml
from commands import update_packages, install_packages

with open('yaml/packages.yml') as f:
    packages_docker = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/repos.yml') as f:
    repos_docker = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/url.yml') as f:
    url_docker = yaml.load(f, Loader=yaml.FullLoader)


def install_docker():
    update_packages()
    install_packages(
        packages_docker['packages_pre_docker'], "Docker Pre-Instalation")
    docker_curl(url_docker['docker']['url'])
    docker_apt_key()
    docker_repo(repos_docker['docker']['arch'], repos_docker['docker']['url'])
    update_packages()
    install_packages(
        packages_docker['packages_post_docker'], "Docker Post-Instalation")
    check_docker()
    create_group_docker()
    add_group_docker()


def docker_curl(url):
    os.system(" curl -fsSL {0} | sudo apt-key add -".format(url))


def docker_apt_key():
    os.system("sudo apt-key fingerprint 0EBFCD88")


def docker_repo(arch, url):
    os.system("sudo add-apt-repository \
   'deb [arch={0}] {1} \
   $(lsb_release -cs) \
   stable'".format(arch, url))


def check_docker():
    os.system("sudo docker run hello-world")


def create_group_docker():
    os.system("sudo groupadd docker")


def add_group_docker():
    os.system("sudo usermod -aG docker $USER")
