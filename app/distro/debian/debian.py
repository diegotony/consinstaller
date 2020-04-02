import click
from  app.commands.apt_commands import prepare_install, install_packages_apt
@click.group()
def cli():
    pass


@cli.command(help='hello debian')
def install_all():
    print(prepare_install())


@cli.command(help='install package')
def install_default():
    install_packages_apt()