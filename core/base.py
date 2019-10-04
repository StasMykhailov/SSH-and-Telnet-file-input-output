import abc
import datetime
import json
import logging


class BaseClass(metaclass=abc.ABCMeta):
    """
    Base class for file input/output connection. While __init__ get host, port, username and password to connect in
    future by SSH or Telnet.
    """
    def __init__(self, host, port, username, password):  # noqa too-many-arguments
        self.client = None
        logs_filename = f'logs/logs{datetime.datetime.now()}.log'
        logging.basicConfig(filename=logs_filename, level=logging.INFO)
        self.logger = logging.getLogger()
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def write_to_file(self, filename, message):
        """
        Simple method to write in file
        :param filename: path to file on remote server
        :param message: message to write in file on remote server
        """
        return self.execute(filename=filename, command='write_to_file', message=message)

    def read_from_file(self, filename):
        """
        Simple method to read from file
        :param filename: path to file on remote server
        """
        return self.execute(filename=filename, command='read_file')

    @abc.abstractmethod
    def execute(self, filename, command, message=None):
        """
        Abstract method to implement in each connection classes for SSH and Telnet connection.
        :param filename: path to file on remote server
        :param command: command to work with file-read or write etc
        :param message: message to write into file
        """
        pass  # noqa unnecessary-pass

    def output(self, filename=None, output_data=None, error=None):
        """
        Write information in file in JSON format.
        :param filename: path to file on remote server
        :param output_data: information from file or message written int file
        :param error: if error occupies it would be not None
        """
        output_filename = f'output_files/file_with_output{datetime.datetime.now()}.json'
        data = {
            'filename': str(filename),
            'output_data': str(output_data),
            'errors': str(error)
        }
        with open(output_filename, 'w+') as output_file:
            json.dump(data, output_file)
        self.client.close()
