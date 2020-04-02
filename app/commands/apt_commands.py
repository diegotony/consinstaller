from app.commands.commands_utils import prepare_install,install_packages_apt
import yaml

with open('app/yaml/apt/packages.yml') as f:
    packages_apt = yaml.load(f, Loader=yaml.FullLoader)


def execute():
    prepare_install()
    print(packages_apt['default'])
    install_packages_apt(packages_apt['default'])



