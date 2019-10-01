import paramiko

from .base import BaseClass


class SSHConnection(BaseClass):
    def __init__(self, host, port, username, password, look_for_keys=True):   # noqa too-many-arguments
        super().__init__(host, port, username, password, look_for_keys)
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        self.init_error = None
        self.ftp_client = None
        try:
            self.client.connect(
                hostname=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
                look_for_keys=self.look_for_keys,
            )
            self.ftp_client = self.client.open_sftp()
        except paramiko.SSHException as error:
            self.init_error = error
            self.logger.error(error)

    def execute(self, filename, command, message=None):
        if not self.ftp_client and self.init_error:
            return self.output(filename=filename, error=self.init_error)
        file_open_mode = 'r'
        if message and command == 'write_to_file':
            file_open_mode = 'w+'
        try:
            with self.ftp_client.open(filename, file_open_mode) as file_to_execute:
                if file_open_mode == 'r':
                    return self.output(
                        filename=filename,
                        output_data=f'Data from file: {file_to_execute.read()}'
                    )
                if file_open_mode == 'w+' and message:
                    file_to_execute.write(message)
                    return self.output(
                        filename=filename,
                        output_data=f'Data written to file: {message}'
                    )
        except FileNotFoundError:
            error_message = f'Error while reading the file. File with name {filename} not found.'
            self.logger.error(error_message)
            return self.output(filename=filename, error=error_message)
        return self.output(filename=filename, error='Useless command. Please, try again and check your input')
