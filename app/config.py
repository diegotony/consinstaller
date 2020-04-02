import os
import platform
from app.distro.debian.debian import cli as cli_debian
OS_DEB = "debian"

def check_system():
    return platform.linux_distribution()


def os_installation():
    dist = check_system()[0]
    if dist == OS_DEB:
        return cli_debian()
    else:
        print("not supported")
