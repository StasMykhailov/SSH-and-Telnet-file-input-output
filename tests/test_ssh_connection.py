import unittest
from unittest import mock
from core.ssh_connection import SSHConnection

FILE_TO_READ = 'tests/not_empty_test_file.txt'
TEXT_TO_READ = 'test text from not empty file'
FILE_TO_WRITE = 'tests/empty_test_file.txt'
TEXT_TO_WRITE = 'test text written into file'


class TestSSHConnection(unittest.TestCase):
    def setUp(self):
        ssh_connection = SSHConnection(
            port='22',
            host='test_ubuntu',
            username='testuser',
            password='testpassword')
        wrong_user_ssh_connection = SSHConnection(
            port='22',
            host='test_ubuntu',
            username='wrong',
            password='wrong')
        wrong_port_and_host_ssh_connection = SSHConnection(
            port='wrong',
            host='wrong',
            username='testuser',
            password='testpassword')
        self.payload = {
            'ssh_connection': ssh_connection,
            'wrong_user_ssh_connection': wrong_user_ssh_connection,
            'wrong_port_and_host_ssh_connection': wrong_port_and_host_ssh_connection,
        }

    def test_connection_read_file(self):
        ssh_connection = self.payload.get('ssh_connection')
        with mock.patch.object(SSHConnection, 'output', return_value=None):
            ssh_connection.read_from_file(FILE_TO_READ)
            self.assertIsNone(ssh_connection.init_error)
            self.assertIsNotNone(ssh_connection.ftp_client)

    def test_connection_write_file(self):
        ssh_connection = self.payload.get('ssh_connection')
        with mock.patch.object(SSHConnection, 'output', return_value=None):
            ssh_connection.write_to_file(FILE_TO_WRITE, TEXT_TO_WRITE)
            self.assertIsNone(ssh_connection.init_error)
            self.assertIsNotNone(ssh_connection.ftp_client)

    def test_wrong_user_connection_read_file(self):
        ssh_connection = self.payload.get('wrong_user_ssh_connection')
        with mock.patch.object(SSHConnection, 'output', return_value=None):
            ssh_connection.read_from_file(FILE_TO_READ)
            self.assertIsNotNone(ssh_connection.init_error)
            self.assertIsNone(ssh_connection.ftp_client)

    def test_wrong_user_connection_write_file(self):
        ssh_connection = self.payload.get('wrong_user_ssh_connection')
        with mock.patch.object(SSHConnection, 'output', return_value=None):
            ssh_connection.write_to_file(FILE_TO_WRITE, TEXT_TO_WRITE)
            self.assertIsNotNone(ssh_connection.init_error)
            self.assertIsNone(ssh_connection.ftp_client)

    def test_wrong_port_and_host_connection_read_file(self):
        ssh_connection = self.payload.get('wrong_port_and_host_ssh_connection')
        with mock.patch.object(SSHConnection, 'output', return_value=None):
            ssh_connection.read_from_file(FILE_TO_READ)
            self.assertIsNotNone(ssh_connection.init_error)
            self.assertIsNone(ssh_connection.ftp_client)

    def test_wrong_port_and_host_connection_write_file(self):
        ssh_connection = self.payload.get('wrong_port_and_host_ssh_connection')
        with mock.patch.object(SSHConnection, 'output', return_value=None):
            ssh_connection.write_to_file(FILE_TO_WRITE, TEXT_TO_WRITE)
            self.assertIsNotNone(ssh_connection.init_error)
            self.assertIsNone(ssh_connection.ftp_client)
