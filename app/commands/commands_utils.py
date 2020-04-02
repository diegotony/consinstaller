from app.commands.Command import Command


def prepare_install():
    Command(package_source="apt", command="update", package="", args="").execute_command_root()


def install_package_apt(sudo, package):
    if sudo:
        Command("apt", "install", package, "-y > /dev/null 2>&1").install_package_root()
    else:
        Command("apt", "install", package, "-y > /dev/null 2>&1").install_package()


def install_packages_apt(packages_list):
    for package in packages_list:

        install_package_apt(True, package)
