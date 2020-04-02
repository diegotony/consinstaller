import click
# from install_docker import install_docker
# from install_fast import install_all
# from utils import packages_gui, message_gui, message_click_colors, message_click
# from install_node import install_node, install_node_all
# from install_minikube import install_k8s_minikube
import platform

@click.group()
def cli():
    pass


# @cli.command(help='Install all apt packages')
# def all():
#     install_all()


# @cli.command(help='Install only apt sysadmin packages (htop,etc)')
# def sys():
#     install_sys()


# @cli.command(help='Install apt basic packages (git,etc)')
# def basic():
#     install_basic()


# @cli.command(help='Install docker ')
# def docker():
#     install_docker()


# @cli.command(help='Install minikube ')
# def minikube():
#     install_k8s_minikube()


# @cli.command(help='Install NodeJs')
# @click.option('--version', default=10, help='Install nodejs 10')
# def nodejs(version):
#     install_node(version)


# @cli.command(help='Install NodeJs with packages')
# @click.option('--version', default=10, help='Install nodejs 10')
# def nodejs_all(version):
#     install_node_all(version)


# @cli.command(help='Download important repositories')
# def github():
#     print("github")



if __name__ == "__main__":
    cli()
