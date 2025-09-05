import datetime
import getpass

from StorageType import StorageType
from StorageHandler import StorageHandler


class MediaFile:
    """Базовый класс для медиа-файлов"""
    def __init__(self, path, storage_type: StorageType,storage_handler: StorageHandler):
        self.path = path
        self.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.owner = getpass.getuser()
        self.storage_type = storage_type
        self.storage_handler = storage_handler
        print(f'Media file has been created: {self}')

    def download(self, from_path):
        return self.storage_handler.download_file(from_path, self.path)

    def upload(self, to_path: str):
        return self.storage_handler.upload_file(self.path, to_path)

    def delete(self):
        return self.storage_handler.delete_file(self.path)

    def __str__(self):
        return f'path: {self.path}, creation_date: {self.creation_date}, owner: {self.owner}'

