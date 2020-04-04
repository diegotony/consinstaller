import click
from app.commands.apt_commands import execute as apt_install
from app.commands.install_docker import execute as docker_install
from app.format.message_cli import init_cli as head
from app.commands.install_node import execute_install_node
from app.commands.install_node import execute_install_node_all


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


@cli.command(help='install NodeJs')
@click.option('--version', default=10, help='Install nodejs 10')
def install_node(version):
    head()
    execute_install_node(version)

@cli.command(help='install NodeJs with modules')
@click.option('--version', default=10, help='Install nodejs 10')
def install_node_all(version):
    head()
    execute_install_node_all(version)