import click
from install_docker import install_docker
from install_fast import install_fast


@click.group()
def main():
    """
    oka
    """
    pass


@main.command()
def fast():
    install_fast()

@main.command()
def docker():
    install_docker()


if __name__ == "__main__":
    main()



