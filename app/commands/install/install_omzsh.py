from app.commands.commands_utils import *
from app.commands.command_class import Command
from app.format.message_cli import step, separator
import yaml

with open("app/yaml/pkg/url.yml") as f:
    urls = yaml.load(f, Loader=yaml.FullLoader)


def execute():
    Command('sh', "-c", '"$(curl -fsSL {0})"'.format(urls["oh-my-zsh"]["url"]), "").execute_command()
    # print(urls["oh-my-zsh"]["url"])
    pass
