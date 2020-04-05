import sys
import os
import click
import yaml
from commands import update_packages, install_packages_apt, install_apt
from utils import message_click_colors, message_click


with open('yaml/packages.yml') as f:
    package = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/repos.yml') as f:
    repos = yaml.load(f, Loader=yaml.FullLoader)

with open('yaml/url.yml') as f:
    url = yaml.load(f, Loader=yaml.FullLoader)


def install_k8s_minikube():
    message_click(
        "\n(¯`·._.··¸.-~*´¨¯¨`*·~-.,-(_Minikube Instalation_)-,.-~*´¨¯¨`*·~-.¸··._.·´¯)\n", "cyan")
    install_kubectl()
    install_kvm()
    install_minikube()


def install_kubectl():
    message_click(
        "\n(¯`·._.··¸.-~*´¨¯¨`*·~-.,-(_Kubectl Instalation_)-,.-~*´¨¯¨`*·~-.¸··._.·´¯)\n", "cyan")
    update_packages()
    install_apt(package['packages_pre_kubectl'])
    kubectl_curl(url['kubectl']['url'])
    kubectl_sources()
    update_packages()
    install_apt(package['packages_post_kubectl'])


def kubectl_curl(url):
    os.system(
        "curl -s {0} | sudo pkg-key add -  > /dev/null".format(url))


def kubectl_sources():
    os.system('echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/pkg/sources.list.d/kubernetes.list')


def install_kvm():
    update_packages()
    install_packages_apt(package['packages_pre_kvm'], "Kvm")


def minikube_direct():
    os.system(' curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
   && sudo install minikube-linux-amd64 /usr/local/bin/minikube')


def install_minikube():
    minikube_direct()

