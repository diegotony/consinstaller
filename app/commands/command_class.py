import os
from app.format.message_cli import *


class Command:

    def __init__(self, arg1, arg2, arg3, args):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.args = args

    def install_package(self):
        cmd = os.system("{0} {1} {2} {3}".format(
            self.arg1,
            self.arg2,
            self.arg3,
            self.args))

        message_state(self.arg3)

        if cmd == 0:
            message_install_correct(self.arg3)
        else:
            message_install_error(self.arg3)

    def install_package_root(self):
        cmd = os.system('sudo {0} {1} {2} {3}'.format(
            self.arg1,
            self.arg2,
            self.arg3,
            self.args))

        message_state(self.arg3)

        if cmd == 0:
            message_install_correct(self.arg3)
        else:
            message_install_error(self.arg3)

    def execute_command(self):
        cmd = os.system("{0} {1} {2} {3}".format(
            self.arg1,
            self.arg2,
            self.arg3,
            self.args))

        message_state(self.arg3)
        if cmd == 0:
            message_execute_correct(self.arg3)
        else:
            message_execute_error(self.arg3)

    def execute_command_root(self):
        cmd = os.system("sudo {0} {1} {2} {3}".format(
            self.arg1,
            self.arg2,
            self.arg3,
            self.args))

        message_state(self.arg3)
        if cmd == 0:
            message_execute_correct(self.arg3)
        else:
            message_execute_error(self.arg3)

    def str_command(self):
        command = "{0} {1} {2} {3}".format(self.arg1, self.arg2, self.arg3, self.args)
        return command
