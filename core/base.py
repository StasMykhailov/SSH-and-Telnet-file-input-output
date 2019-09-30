import abc
import datetime
import json
import logging


class BaseClass(metaclass=abc.ABCMeta):

    def __init__(self, host, port, username, password):
        logs_filename = 'logs{}.log'.format(datetime.datetime.now)
        logging.basicConfig(filename=logs_filename, level=logging.INFO)
        self.logger = logging.getLogger()
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    @abc.abstractmethod
    def execute(self):
        pass

    def output(self, input_data, output_data, errors):
        filename = '{}{}.txt'.format('output', datetime.datetime.now())
        data = {
            'input_data': input_data,
            'output_data': output_data,
            'errors': errors
        }
        with open(filename, 'w+') as output_file:
            json.dump(data, output_file)
