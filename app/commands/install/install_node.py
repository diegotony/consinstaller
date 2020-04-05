import yaml
from app.commands.commands_utils import install_packages_apt, prepare_install, install_package_apt, join_commands
from app.format.message_cli import step, separator
from app.commands.command_class import Command

with open("app/yaml/pkg/packages.yml") as f:
    packages = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/pkg/url.yml') as f:
    url = yaml.load(f, Loader=yaml.FullLoader)


def execute_install_node(version):
    separator("NodeJs Instalation")
    step("Updating Packages")
    prepare_install()
    step("Adding Repository ... ")
    node_curl(url['nodejs']['url'], version)
    step("Installing Node")
    install_package_apt(True, packages['packages_pre_node'])


def execute_install_node_all(version):
    separator("NodeJs Instalation")
    step("Updating Packages")
    prepare_install()
    step("Adding Repository ... ")
    node_curl(url['nodejs']['url'], version)
    step("Installing Node")
    install_package_apt(True, packages['packages_pre_node'])
    step("Installing Node Modules")
    install_packages_npm(packages['packages_npm'])


def node_curl(link, version):
    cmd1 = Command("curl", "-sL", "{0}{1}.x".format(link, version), "")
    cmd2 = Command("sudo ", "-E", "bash", "-")
    join_commands(cmd1, "|", cmd2)


def install_npm(package):
    Command("npm", "i -g", "{0}".format(package), "-y > /dev/null 2>&1").install_package_root()


def install_packages_npm(packages_list):
    for package in packages_list:
        install_npm(package)
