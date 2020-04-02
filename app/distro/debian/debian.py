import click
from app.commands.apt_commands import execute as apt_install_packages_default
from app.commands.install_docker import execute as docker_install

@click.group()
def cli():
    pass


@cli.command(help='install packages default')
def default():
    # apt_install_packages_default()
    docker_install()


# def with_docker(help="install packages default and docker"):
#     prepare_install()
#
#     pass
# # @cli.command(help='install package')
# def install_default():
#     install_packages_apt()
