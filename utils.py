from pyfiglet import Figlet, figlet_format
import os
import click


def init_cli():
    message_click("@xxxx[{::::::::::::::::::::::::::::::::::> ", "red")
    message_click("\,,/.<(*_*)> live long and prosper", "green")
    message_click("@xxxx[{::::::::::::::::::::::::::::::::::> ", "blue")



def packages_gui(name):
    result = figlet_format("Packages {0}".format(name), font="digital")
    return result


def message_gui(name):
    result = figlet_format("{0}".format(name), font="digital")
    return result


def message_click_colors(message, bg, fg):
    click.echo(click.style(' {0} '.format(message),
                           fg='{0}'.format(fg),
                           bg='{0}'.format(bg),
                           bold=True), err=True)


def message_click(message, fg):
    click.echo(click.style(' {0} '.format(message),
                           fg='{0}'.format(fg),
                           bold=True), err=True)
