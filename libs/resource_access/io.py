import _io
from abc import ABCMeta

JOB_DATABASE_ROOT = 'storage/jobs.json'


class RawFileIO(metaclass=ABCMeta):
    file_root: str
    fd: _io.TextIOWrapper

    def __init__(self, file_root: str):
        self.file_root = file_root
        self.fd = None

    def __enter__(self, mode: str):
        self.fd = open(self.file_root, mode=mode)
        return self.fd

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fd.close()
        self.fd = None


class RawFileRead(RawFileIO):

    def __enter__(self, mode: str = None):
        return super().__enter__('rt')


class RawFileWrite(RawFileIO):

    def __enter__(self, mode: str = None):
        return super().__enter__('wt')


class JobDatabaseRead(RawFileRead):

    def __init__(self):
        super().__init__(JOB_DATABASE_ROOT)


class JobDatabaseWrite(RawFileWrite):

    def __init__(self):
        super().__init__(JOB_DATABASE_ROOT)
