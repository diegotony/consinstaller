from pyfiglet import Figlet, figlet_format
import click


def message_color(string_message, bg, fg):
    click.echo(click.style(' {0} '.format(string_message),
                           fg='{0}'.format(fg),
                           bg='{0}'.format(bg),
                           bold=True), err=True)


def message(string_message, fg):
    click.echo(click.style(' {0} '.format(string_message),
                           fg='{0}'.format(fg),
                           bold=True), err=True)


def package_message(name):
    result = figlet_format("Packages {0}".format(name), font="digital")
    return result


def message_gui(name):
    result = figlet_format("{0}".format(name), font="digital")
    return result


def init_cli():
    message("@xxxx[{::::::::::::::::::::::::::::::::::> ", "red")
    message("\,,/.<(*_*)> live long and prosper", "green")
    message("@xxxx[{::::::::::::::::::::::::::::::::::> ", "blue")