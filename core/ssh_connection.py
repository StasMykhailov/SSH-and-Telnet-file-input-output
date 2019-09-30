import paramiko

from .base import BaseClass


class SSHConnection(BaseClass):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.client = paramiko.SSHClient()

