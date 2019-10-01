import abc
import datetime
import json
import logging


class BaseClass(metaclass=abc.ABCMeta):

    def __init__(self, host, port, username, password, look_for_keys):  # noqa too-many-arguments
        logs_filename = 'logs/logs{}.log'.format(datetime.datetime.now())
        logging.basicConfig(filename=logs_filename, level=logging.INFO)
        self.logger = logging.getLogger()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.look_for_keys = look_for_keys

    def write_to_file(self, filename, message):
        return self.execute(filename=filename, command='write_to_file', message=message)

    def read_from_file(self, filename):
        return self.execute(filename=filename, command='read_file')

    @abc.abstractmethod
    def execute(self, filename, command, message=None):
        pass

    def output(self, filename=None, output_data=None, error=None):
        output_filename = f'output_files/file_with_output{datetime.datetime.now()}.json'
        data = {
            'filename': str(filename),
            'output_data': str(output_data),
            'errors': str(error)
        }
        with open(output_filename, 'w+') as output_file:
            json.dump(data, output_file)
