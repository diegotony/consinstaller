from app.commands.commands_utils import prepare_install,install_packages_apt
import yaml

with open('app/yaml/pkg/packages.yml') as f:
    packages_apt = yaml.load(f, Loader=yaml.FullLoader)


def execute():
    prepare_install()
    install_packages_apt(packages_apt['default'])



