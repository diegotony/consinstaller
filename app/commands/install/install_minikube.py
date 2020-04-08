import yaml
from app.commands.commands_utils import *
from app.format.message_cli import *

with open('app/yaml/pkg/packages.yml') as f:
    package = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/pkg/repos.yml') as f:
    repos = yaml.load(f, Loader=yaml.FullLoader)

with open('app/yaml/pkg/url.yml') as f:
    url = yaml.load(f, Loader=yaml.FullLoader)


def execute():
    separator("Minikube Installation")
    install_kubectl()
    install_kvm()
    install_minikube()


def kubectl_curl(url):
    cmd1 = Command('curl', '-s', 'https://packages.cloud.google.com/apt/doc/apt-key.gpg', '')
    cmd2 = Command('sudo', 'apt-key', 'add', '-')
    join_commands(cmd1, '|', cmd2)


def kubectl_add_repos():
    cmd1 = Command('echo', '"deb https://apt.kubernetes.io/ kubernetes-xenial main"', '', '')
    cmd2 = Command('sudo', 'tee', '-a', '/etc/apt/sources.list.d/kubernetes.list')
    join_commands(cmd1, '|', cmd2)


def install_kubectl():
    step("Update Package..")
    prepare_install()
    step('Installing KubeCTL')
    install_packages_apt(package['packages_pre_kubectl'])
    step("Added Curl KubeCTL")
    kubectl_curl(url['kubectl']['url'])
    step('Added repos KubeCTL')
    kubectl_add_repos()
    step("Update Package..")
    prepare_install()
    step('Installing KubeCTL')
    install_package_apt(True, package['packages_post_kubectl'])


def install_kvm():
    step('Installing KVM')
    step("Update Package..")
    prepare_install()
    step('Installing KVM')
    install_package_apt(True, package['packages_pre_kvm'])


def install_minikube():
    cmd1 = Command('curl', '-LO', 'https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64', '')
    cmd2 = Command('sudo', 'install', 'minikube-linux-amd64', '/usr/local/bin/minikube')
    join_commands(cmd1, '&&', cmd2)

