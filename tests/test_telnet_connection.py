import unittest

FILE_TO_READ = 'tests/not_empty_test_file.txt'
TEXT_TO_READ = 'test text from not empty file'
FILE_TO_WRITE = 'tests/empty_test_file.txt'
TEXT_TO_WRITE = 'test text written into file'


class TestTelnet(unittest.TestCase):
    def test(self):
        self.skipTest('Problems with docker container')
