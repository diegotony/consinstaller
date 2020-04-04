import click
from app.commands.apt_commands import execute as apt_install
from app.commands.install_docker import execute as docker_install
from app.format.message_cli import init_cli as head

@click.group()
def cli():
    pass


@cli.command(help='install apt')
def default():
    head()
    apt_install()


@cli.command(help='install docker')
def install_docker():
    head()
    docker_install()

# def with_docker(help="install packages default and docker"):
#     prepare_install()
#
#     pass
# # @cli.command(help='install package')
# def install_default():
#     install_packages_apt()
