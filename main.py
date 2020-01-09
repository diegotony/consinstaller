from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
from utils import init_cli, install_packages
import yaml
from commands import init_install, root,exit

with open('questions/install.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

if __name__ == "__main__":
    # print(questions_install)
    print(init_cli())
    answers_install = prompt(data['questions']['install'])
    if answers_install['install'] == 'Quick':
        init_install()
        install_packages(data['packages_default'])
    if answers_install['install'] == 'Manual':
        questions_envs = [
            # Allows you have a list of choices
            # Furthermore you can refer to the documentation.
            {
                'type': 'checkbox',
                'message': 'Select the envs to install',
                'name': 'toppings',
                'choices': [
                    {
                        'name': 'SysAdmin'
                    },
                    {
                        'name': 'Node'
                    },
                    {
                        'name': 'Docker'
                    },
                    {
                        'name': 'minikube'
                    },
                    {
                        'name': 'Utils'
                    },

                ],
                'validate': lambda answer: 'You must choose at least one topping.' \
                if len(answer) == 0 else True
            }

        ]
        answers_install = prompt(questions_envs)

    pass
