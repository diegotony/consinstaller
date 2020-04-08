import yaml
from app.commands.commands_utils import *
from app.format.message_cli import *

with open('app/yaml/pkg/packages.yml') as f:
    packages = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/pkg/repos.yml') as f:
    repos = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/pkg/url.yml') as f:
    urls = yaml.load(f, Loader=yaml.FullLoader)


def execute():
    separator("Docker Installation")
    step("Preparing Install...")
    step("Update Package..")
    prepare_install()
    step("Installing Docker dependencies")
    install_packages_apt(packages['packages_pre_docker'])
    step("Added Docker’s official GPG key")
    docker_curl(urls['docker']['url'])
    step("Verify fingerprint GPG")
    docker_apt_key()
    step("Adding Repository to sources_list...")
    add_repo(repos['docker']['arch'], repos['docker']['url'])
    step("Update Package.. (Again)")
    prepare_install()
    step("Installing Docker")
    install_packages_apt(packages['packages_post_docker'])
    step("Testing Docker Installation")
    check_docker()
    step("Create Docker Group")
    create_group_docker()
    step("Add User to Docker Group")
    add_group_docker()


def docker_curl(url):
    cmd1 = Command("curl", "-fsSL", url, "")
    cmd2 = Command("sudo", "key", "add", "-")
    join_commands(cmd1, "|", cmd2)


def docker_apt_key():
    Command("pkg-key", "fingerprint", "0EBFCD88", "").execute_command_root()


def check_docker():
    Command('docker', 'run', 'hello-world', "").execute_command_root()


def create_group_docker():
    Command("groupadd", "docker", "", "").execute_command_root()


def add_group_docker():
    Command('usermod', '-aG ', 'docker $USER', "").execute_command_root()
