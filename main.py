from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
from utils import init_cli
import yaml
questions_envs = ""

with open('questions/install.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    questions_envs = data['questions_envs']

if __name__ == "__main__":
    # print(questions_install)
    print(init_cli())
    answers_install = prompt(data['questions_install'])
    if answers_install['install'] == 'Quick':
        # anwsers_envs = prompt(questions_envs)
        print(questions_envs)
    pass
