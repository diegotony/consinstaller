import click
from install_docker import install_docker
from install_fast import install_all, install_sys, install_basic
from utils import packages_gui, message_gui, message_click_colors, message_click


@click.group()
def cli():
    pass


@cli.command(help='Install all apt packages')
def all():
    install_all()


@cli.command(help='Install only apt sysadmin packages (htop,etc)')
def sys():
    install_sys()


@cli.command(help='Install apt basic packages (git,etc)')
def basic():
    install_basic()


@cli.command(help='Install docker ')
def docker():
    install_docker()


@cli.command(help='Install minikube ')
def minikube():
    print("nminikube")


@cli.command(help='Install Nodejs')
def nodejs():
    print("node")


@cli.command(help='Download important repositories')
def github():
    print("github")


@cli.command(help='Install apt, docker, nodejs ')
def allall():
    print(message_click_colors(
        '           ,.-~*´¨¯¨`*·~-.¸-(_Phase_One_)-,.-~*´¨¯¨`*·~-.¸         ', 'white', "black"))
    install_all()
    print(message_click_colors(
        '           ,.-~*´¨¯¨`*·~-.¸-(_Phase_Two_)-,.-~*´¨¯¨`*·~-.¸         ', 'white', "black"))
    install_docker()


if __name__ == "__main__":
    cli()
