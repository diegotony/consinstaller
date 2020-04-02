from app.commands.Command import Command


def prepare_install():
    Command("apt", "update", "", "").execute_command_root()


def install_package_apt(sudo, package):
    if sudo:
        Command("apt", "install", package, "-y > /dev/null 2>&1").install_package_root()
    else:
        Command("apt", "install", package, "-y > /dev/null 2>&1").install_package()


def join_commands(command_one, operator, command_two):
    Command(command_one.str_command(), operator, command_two.str_command(), "").execute_command()


def add_repo(arch, url):
    Command("add-apt-repository",  " 'deb [arch={0}] {1} \
            buster \
            stable'" .format(arch, url), "", "").execute_command_root()


def install_packages_apt(packages_list):
    for package in packages_list:
        install_package_apt(True, package)
