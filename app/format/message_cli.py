from pyfiglet import Figlet, figlet_format
import click
from functools import wraps


# def message_color(string_message, bg, fg):
#     click.echo(click.style(' {0} '.format(string_message),
#                            fg='{0}'.format(fg),
#                            bg='{0}'.format(bg),
#                            bold=True), err=True)


def message(string_message, fg):
    click.echo(click.style(' {0} '.format(string_message),
                           fg='{0}'.format(fg),
                           bold=True), err=True)


# CLI messages
def message_state(string_message):
    click.echo(style('Executing {0} ...'.format(string_message), "yellow"), err=True)


def step(string_name):
    return message("STEP:\t" + string_name.upper(), "white")


def package_message(name):
    result = figlet_format("Packages {0}".format(name), font="digital")
    return result


def message_gui(name):
    result = figlet_format("{0}".format(name), font="digital")
    return result


def separator(name):
    message(
        "(¯`·._.··¸.-~*´¨¯¨`*·~-.,-(_{0}_)-,.-~*´¨¯¨`*·~-.¸··._.·´¯)\n".format(name), "cyan")


def init_cli():
    print("\n" + style("\t\t\t@xxxx[{::::::::::::::::::::::::::::::::::>", "red") + "\n" +
          style("\t\t\t\,,/.<(*_*)> live long and prosper", "green") + "\n" +
          style("\t\t\t@xxxx[{::::::::::::::::::::::::::::::::::> ", "blue") + "\n")


def style(name, fg):
    return click.style('{0}'.format(name), fg='{0}'.format(fg), bold=True)


def message_install_correct(string_message):
    click.echo(style(("==> {0} ").format(string_message), "magenta") +
               style(("INSTALLED ").format(string_message), "cyan") +
               style(("\t\t \,,/(^_^)\,,/ ").format(string_message), "magenta"),
               err=True)


def message_execute_correct(string_message):
    click.echo(style(("==> {0} ").format(string_message), "magenta") +
               style(("CORRECT ").format(string_message), "cyan") +
               style(("\t\t \,,/(^_^)\,,/ ").format(string_message), "magenta"),
               err=True)


def message_install_error(string_message):
    click.echo(style(("==> {0} ").format(string_message), "magenta") +
               style(("NOT INSTALLED ").format(string_message), "red") +
               style(("\t\t <*_*>").format(string_message), "magenta"),
               err=True)


def message_execute_error(string_message):
    click.echo(style(("==> {0} ").format(string_message), "magenta") +
               style(("UPPS").format(string_message), "red") +
               style(("\t\t <*_*>").format(string_message), "magenta"),
               err=True)
