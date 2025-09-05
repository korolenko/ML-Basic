from abc import ABC

from StorageHandler import StorageHandler

class S3StorageHandler(StorageHandler, ABC):
    """Реализация работы с S3"""

    def __init__(self):
        print('S3StorageHandler created')

    def upload_file(self, local_path: str, remote_path: str):
        print(f'S3StorageHandler: file {local_path} is uploaded to {remote_path}')

    def download_file(self, remote_path: str, local_path: str):
        print(f'S3StorageHandler: file {remote_path} is downloaded to {local_path}')

    def delete_file(self, path: str):
        print(f'S3StorageHandler: file {path} is deleted')

