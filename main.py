from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
import yaml
import click
from utils import init_cli, install_packages
from commands import init_install, root, exit
from install_docker import install_docker


with open('yaml/packages.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


@click.group()
def main():
    """
    oka
    """
    pass


@main.command()
def fast():
    print(init_cli())
    init_install()
    install_packages(data['packages_default'], "Default")
    install_packages(data['packages_admin'], "SysAdmin")
    install_packages(data['packages_utils'], "Utils")


# @click.command()
# @click.argument('manual')
# def fast(manual):
#     questions_envs = [
#         # Allows you have a list of choices
#         # Furthermore you can refer to the documentation.
#         {
#             'type': 'checkbox',
#             'message': 'Select the envs to install',
#             'name': 'toppings',
#             'choices': [
#                 {
#                     'name': 'SysAdmin'
#                 },
#                 {
#                     'name': 'Node'
#                 },
#                 {
#                     'name': 'Docker'
#                 },
#                 {
#                     'name': 'minikube'
#                 },
#                 {
#                     'name': 'Utils'
#                 },

#             ],
#             'validate': lambda answer: 'You must choose at least one topping.' \
#             if len(answer) == 0 else True
#         }

#     ]
#     answers_install = prompt(questions_envs, style=style)


@main.command()
def docker():
    install_docker()


if __name__ == "__main__":
    main()


# if __name__ == "__main__":
#     # print(questions_install)
#     print(init_cli())
#     answers_install = prompt(data['questions']['install'],style=style)
#     if answers_install['install'] == 'Quick':
#         init_install()
#         install_packages(data['packages_default'],"Default")
#     if answers_install['install'] == 'Manual':

#     pass
