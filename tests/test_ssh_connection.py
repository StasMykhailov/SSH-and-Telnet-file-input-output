import unittest

from core.ssh_connection import SSHConnection


class TestSomething(unittest.TestCase):

    def test_it(self):
        ssh_connection = SSHConnection(
            port='22',
            host='test_ubuntu',
            username='testuser',
            password='testpassword')
        print(ssh_connection.init_error)
        print(ssh_connection.ftp_client)
        ssh_connection.write_to_file('test.txt', 'tst')
        self.assertEqual(False, True)

