from app.commands.Command import Command
import yaml

with open('app/yaml/apt/packages.yml') as f:
    packages_apt = yaml.load(f, Loader=yaml.FullLoader)


def prepare_install():
    Command("apt", "update", "").execute_root()


def install_package_apt(package):
    Command("apt", "install", package, "-y > /dev/null 2>&1").execute_root()


def install_packages_apt():
    packages_list = packages_apt['packages_default']
    for package in packages_list:
        install_package_apt(package)
