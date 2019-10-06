from telnetlib import Telnet

from .base import BaseClass


class TelnetConnection(BaseClass):
    def __init__(self, host, port, username, password):
        """
        Try to connect by Telnet to remote server and set attribute client and ftp_client if connected.
        If not, set attribute init_error to error raised by connection.
        :param host: host of the server
        :param port: port of the server
        :param username: username from server
        :param password: password for user from server
        """
        super().__init__(host, port, username, password)
        self.client = None
        self.init_error = None
        try:
            self.client = Telnet(host)
            self.client.read_until('Username : ')
            self.client.write(f'{username}\r')
            self.client.read_until('Password : ')
            self.client.write(f'{password}\n')
            self.client.write('\r')
        except OSError as error:
            self.init_error = error
            self.logger.error(error)

    def execute(self, filename, command, message=None):
        """
        Write to file or read from file according to command.
        :param filename: path to file on remote server
        :param command: command to work with file-read or write etc
        :param message: message to write into file
        """
        if not self.client and self.init_error:
            return self.output(filename=filename, error=self.init_error)
        if command == 'read_file':
            try:
                self.client.write(f'cat {filename}')
                self.client.write('\n')
                data_from_file = self.client.read_eager()
                return self.output(
                    filename=filename,
                    output_data=f'Data from file: {data_from_file}'
                )
            except Exception as error:
                return self.output(filename=filename, error=f'Got error {error}')
        if command == 'write_to_file':
            if not message:
                return self.output(filename=filename, error='Got no message ti write to file')
            try:
                self.client.write(f'echo {message} >> {filename}')
                return self.output(
                    filename=filename,
                    output_data=f'Data written to file: {message}'
                )
            except Exception as error:
                return self.output(filename=filename, error=f'Got error {error}')

        return self.output(filename=filename, error='Useless command. Please, try again and check your input')
