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


def message_state(string_message):
    click.echo(click.style('Executing {0} ...'.format(string_message),
                           fg='yellow',
                           bold=True), err=True)

    pass


def message_install_correct(string_message):
    click.echo(click.style('==>  {0} Installed\t\t \,,/(^_^)\,,/ '.format(string_message),
                           fg='green',
                           bold=True), err=True)


def message_execute_correct(string_message):
    click.echo(click.style('==>  {0} correct\t\t \,,/(^_^)\,,/ '.format(string_message),
                           fg='green',
                           bold=True), err=True)


def message_install_error(string_message):
    click.echo(click.style('==>  {0} not installed\t\t <*_*>'.format(string_message),
                           fg='red',
                           bold=True), err=True)


def message_execute_error(string_message):
    click.echo(click.style('==>  {0} Upps\t\t <*_*>'.format(string_message),
                           fg='red',
                           bold=True), err=True)


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
    message("@xxxx[{::::::::::::::::::::::::::::::::::> ", "red")
    message("\,,/.<(*_*)> live long and prosper", "green")
    message("@xxxx[{::::::::::::::::::::::::::::::::::> ", "blue")
