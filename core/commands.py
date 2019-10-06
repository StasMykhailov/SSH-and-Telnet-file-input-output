import sys

from core.base import BaseClass
from core.ssh_connection import SSHConnection
from core.telnet_connection import TelnetConnection


class ConnectionCommand(BaseClass):
    """
    Create connection and execute method based on arguments from bash command
    """
    def __init__(self):
        self.init_error = None
        try:
            super().__init__(host=sys.argv[2], port=sys.argv[3], username=sys.argv[4], password=sys.argv[5])
            self.method = sys.argv[1].upper()
            self.command = sys.argv[6].upper()
            self.filename = sys.argv[7]
        except IndexError as error:
            self.init_error = error
        try:
            self.message = sys.argv[8]
        except IndexError:
            self.message = None
        try:
            if self.method == 'SSH':
                self.connection = SSHConnection(
                    port='22',
                    host='test_ubuntu',
                    username='testuser',
                    password='testpassword')
            elif self.method == 'TELNET':
                self.connection = TelnetConnection(
                    port='22',
                    host='test_ubuntu',
                    username='testuser',
                    password='testpassword')
            else:
                self.init_error = 'Unknown method'
        except Exception as error:
            self.init_error = error

    def execute(self, filename, command, message=None):
        if self.init_error:
            return self.output(filename=self.filename, error=self.init_error)
        if self.command == 'READ':
            return self.connection.read_from_file(self.filename)
        if self.command == 'WRITE':
            return self.connection.write_to_file(self.filename, self.message)
        return self.output(filename=self.filename, error=f'Method:{self.method} with unknown command')


if __name__ == '__main__':
    run_command = ConnectionCommand()
    run_command.execute(filename=None, command=None)
