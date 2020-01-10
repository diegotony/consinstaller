import click
from install_docker import install_docker
from install_fast import install_fast
from utils import packages_gui, message_gui, message_click_colors, message_click


@click.group()
def main():
    """
    oka
    """
    pass


@main.command()
def fast():
    print(message_click_colors(
        '           ,.-~*´¨¯¨`*·~-.¸-(_Phase_One_)-,.-~*´¨¯¨`*·~-.¸         ', 'white', "black"))
    install_fast()
    print(message_click_colors(
        '           ,.-~*´¨¯¨`*·~-.¸-(_Phase_Two_)-,.-~*´¨¯¨`*·~-.¸         ', 'white', "black"))
    install_docker()


@main.command()
def docker():
    install_docker()


if __name__ == "__main__":
    main()
