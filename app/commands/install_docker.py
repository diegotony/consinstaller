import sys
import os
import click
import yaml
from app.commands.Command import Command
from app.commands.commands_utils import prepare_install, install_packages_apt
from app.format.message_cli import message

with open('app/yaml/apt/packages.yml') as f:
    packages_docker = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/apt/repos.yml') as f:
    repos_docker = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/apt/url.yml') as f:
    url_docker = yaml.load(f, Loader=yaml.FullLoader)


def execute():
    message(
        "(¯`·._.··¸.-~*´¨¯¨`*·~-.,-(_Docker Instalation_)-,.-~*´¨¯¨`*·~-.¸··._.·´¯)\n", "cyan")

    prepare_install()
    install_packages_apt(packages_docker['packages_pre_docker'])
    message("Added Docker’s official GPG key", "cyan")
    docker_curl(url_docker['docker']['url'])
    message("Verify fingerprint", "cyan")
    docker_apt_key()
    message("Adding Repository ...", "cyan")
    docker_repo(repos_docker['docker']['arch'], repos_docker['docker']['url'])
    prepare_install()
    install_packages_apt(packages_docker['packages_post_docker'])
    message("Testing Docker", "cyan")
    check_docker()
    message("Create docker group", "cyan")
    create_group_docker()
    add_group_docker()


def docker_curl(url):
    Command("curl -fsSL", url, "| ","sudo apt-key add -").execute_command_root()
    # os.system(" curl -fsSL {0} | sudo apt-key add -".format(url))


def docker_apt_key():
    Command("apt-key", "fingerprint", "0EBFCD88", "").execute_command_root()
    # os.system("sudo apt-key fingerprint 0EBFCD88")


def docker_repo(arch, url):
    Command('add-apt-repository',
            " 'deb [arch={0}] {1} \
            buster \
            stable'"
            .format(arch, url), "", "").execute_command_root()


#  os.system("sudo add-apt-repository \
# 'deb [arch={0}] {1} \
# buster \
# stable'".format(arch, url))


def check_docker():
    Command('docker', 'run', 'hello-world', "").execute_command_root()


def create_group_docker():
    Command("groupadd", "docker", "", "").execute_command_root()
    # os.system("sudo groupadd docker")


def add_group_docker():
    Command('usermod', '-aG ', 'docker $USER', "").execute_command_root()
    # os.system("sudo usermod -aG docker $USER")
