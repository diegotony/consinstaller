import os
from app.format.message_cli import message


class Command:

    def __init__(self, package_source, command, package, args):
        self.package_source = package_source
        self.command = command
        self.package = package
        self.args = args

    def install_package(self):
        cmd = os.system("{0} {1} {2} {3}".format(
            self.package_source,
            self.command,
            self.package,
            self.args))

        message(('Installing {0} ...'.format(self.package)), "yellow")

        if cmd == 0:
            message(('==>  {0} installed    \,,/(^_^)\,,/ '.format(self.package)), "green")

        else:
            message(('==>  {0} not installed    <*_*>  '.format(self.package)), "red")

    def install_package_root(self):
        cmd = os.system('sudo {0} {1} {2} {3}'.format(
            self.package_source,
            self.command,
            self.package,
            self.args))

        message(('Installing {0} ...'.format(self.package))
                , "yellow")
        if cmd == 0:
            message(('==>  {0} installed    \,,/(^_^)\,,/ '.format(self.package)), "green")

        else:
            message(('==>  {0} not installed    <*_*>  '.format(self.package)), "red")

    def execute_command(self):
        cmd = os.system("{0} {1} {2} {3}".format(
            self.package_source,
            self.command,
            self.package,
            self.args))

        message(('Execute {0} {1} {2} {3} ...'.format(self.package_source,
                                                      self.command,
                                                      self.package,
                                                      self.args)), "yellow")

        if cmd == 0:
            message(('==>  {0} {1} Correct    \,,/(^_^)\,,/ '.format(self.package_source, self.command)), "green")

        else:
            message(('==>  {0} {1}  Upps    <*_*>  '.format(self.package_source,self.command)), "red")

    def execute_command_root(self):
        cmd = os.system("sudo {0} {1} {2} {3}".format(
            self.package_source,
            self.command,
            self.package,
            self.args))

        message(('Execute {0} {1} {2} {3} ...'.format(self.package,
                                                      self.command,
                                                      self.package,
                                                      self.args)), "yellow")

        if cmd == 0:
            message(('==>  {0}  Correct    \,,/(^_^)\,,/ '.format(self.package)), "green")

        else:
            message(('==>  {0} Upps   <*_*>  '.format(self.package)), "red")

    def print_command(self):
        print(self.package_source,
              self.command,
              self.package,
              self.args)
