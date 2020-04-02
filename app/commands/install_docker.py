import yaml
from app.commands.Command import Command
from app.commands.commands_utils import *
from app.format.message_cli import *

with open('app/yaml/apt/packages.yml') as f:
    packages = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/apt/repos.yml') as f:
    repos = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/apt/url.yml') as f:
    urls = yaml.load(f, Loader=yaml.FullLoader)


def execute():
    separator("Docker Installation")
    prepare_install()
    install_packages_apt(packages['packages_pre_docker'])
    message("Added Docker’s official GPG key", "cyan")
    docker_curl(urls['docker']['url'])
    message("Verify fingerprint", "cyan")
    docker_apt_key()
    message("Adding Repository ...", "cyan")
    add_repo(repos['docker']['arch'], repos['docker']['url'])
    prepare_install()
    install_packages_apt(packages['packages_post_docker'])
    message("Testing Docker", "cyan")
    check_docker()
    message("Create docker group", "cyan")
    create_group_docker()
    add_group_docker()


def docker_curl(url):
    cmd1 = Command("curl", "-fsSL", "url", "")
    cmd2 = Command("sudo", "key", "add", "-")
    join_commands(cmd1, "|", cmd2)


def docker_apt_key():
    Command("apt-key", "fingerprint", "0EBFCD88", "").execute_command_root()




def check_docker():
    Command('docker', 'run', 'hello-world', "").execute_command_root()


def create_group_docker():
    Command("groupadd", "docker", "", "").execute_command_root()
    # os.system("sudo groupadd docker")


def add_group_docker():
    Command('usermod', '-aG ', 'docker $USER', "").execute_command_root()
